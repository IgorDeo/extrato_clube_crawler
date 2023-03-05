from .cpf_validator import CPFValidator
import json
import requests
from .exceptions import (
    CPFInvalido,
    CPFNaoInformado,
    LoginNaoInformado,
    SenhaNaoInformada,
    CredenciaisInvalidas,
)

BASE_URL = """http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com"""

LOGIN_ENDPOINT = "/login"
CPF_BENEFICIOS_ENDPOINT = "/offline/listagem/{cpf}"

LOGIN_URL = f"{BASE_URL}{LOGIN_ENDPOINT}"


class BeneficiosCrawler:
    def __init__(self, cpf: str = "", login: str = "", password: str = ""):
        if cpf == "":
            raise CPFNaoInformado("CPF não informado")

        if not CPFValidator.is_valid(cpf):
            raise CPFInvalido("CPF inválido")

        if login == "":
            raise LoginNaoInformado("Login não informado")

        if password == "":
            raise SenhaNaoInformada("Senha não informada")

        self.cpf = CPFValidator.extract_numbers(cpf)
        self.login = login
        self.password = password

    def crawl(self):
        token = self.get_authorization_token()
        beneficios = self.get_beneficios(token)
        beneficios = self.parse_beneficios(beneficios)
        return beneficios

    def get_authorization_token(self):
        form = json.dumps({"login": self.login, "senha": self.password})
        response = requests.post(LOGIN_URL, data=form)
        if response.status_code == 401:
            raise CredenciaisInvalidas("Credenciais de acesso inválidas")
        return response.headers.get("Authorization")

    def get_beneficios(self, token: str):
        response = requests.get(
            url=f"{BASE_URL}{CPF_BENEFICIOS_ENDPOINT.format(cpf=self.cpf)}",
            headers={"Authorization": token},
        )
        return response.json()

    def parse_beneficios(self, dados: dict):
        numeros = []
        beneficios = dados.get("beneficios")
        if beneficios is None or len(beneficios) == 0:
            return numeros

        for beneficio in beneficios:
            numero = beneficio.get("nb")
            if numero is not None:
                numeros.append(numero)

        return numeros
