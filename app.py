from flask import Flask, request


from extrato_clube_crawler.beneficios_crawler import BeneficiosCrawler

app = Flask(__name__)


@app.route("/consulta/<cpf>", methods=["POST"])
def consulta(cpf: str):
    body = request.get_json(force=True)
    login = body.get("login")
    password = body.get("senha")
    crawler = BeneficiosCrawler(cpf, login, password)
    beneficios = crawler.crawl()
    return beneficios
