from extrato_clube_crawler.beneficios_crawler import BeneficiosCrawler
from extrato_clube_crawler.exceptions import (
    CPFInvalido,
    CPFNaoInformado,
    LoginNaoInformado,
    SenhaNaoInformada,
)
import pytest


class TestBeneficiosCrawler:
    def test_quando_criar_um_crawler_deve_retornar_uma_instancia_de_crawler(self):
        cpf = "033.355.888-00"
        login = "login"
        password = "password"
        crawler = BeneficiosCrawler(cpf, login, password)
        assert isinstance(crawler, BeneficiosCrawler)

    def test_quando_criar_um_crawler_sem_informar_o_cpf_deve_retornar_uma_excecao(self):
        cpf = ""
        login = "login"
        password = "password"
        with pytest.raises(CPFNaoInformado):
            BeneficiosCrawler(cpf, login, password)

    def test_quando_criar_um_crawler_com_cpf_invalido_deve_retornar_uma_excecao(self):
        cpf = "033.355.888-01"
        login = "login"
        password = "password"
        with pytest.raises(CPFInvalido):
            BeneficiosCrawler(cpf, login, password)

    def test_quando_criar_um_crawler_sem_informar_o_login_deve_retornar_uma_excecao(
        self,
    ):
        cpf = "033.355.888-00"
        login = ""
        password = "password"
        with pytest.raises(LoginNaoInformado):
            BeneficiosCrawler(cpf, login, password)

    def test_quando_criar_um_crawler_sem_informar_a_senha_deve_retornar_uma_excecao(
        self,
    ):
        cpf = "033.355.888-00"
        login = "login"
        password = ""
        with pytest.raises(SenhaNaoInformada):
            BeneficiosCrawler(cpf, login, password)

    @pytest.mark.parametrize(
        "entrada, esperado",
        [({"beneficios": [{"nb": "123"}, {"nb": "456"}]}, ["123", "456"]), ({}, [])],
    )
    def test_quando_parse_beneficios_eh_chamado(self, entrada, esperado):
        crawler = BeneficiosCrawler("033.355.888-00", "login", "password")
        resultado = crawler.parse_beneficios(entrada)
        print(resultado)
        assert resultado == esperado
