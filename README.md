# Extrato Clube Crawler

## Objetivo:
Esse é um simples crawler que dado um número de CPF e credenciais de login, é feita uma consulta pelos números de benefícios daquele CPF.

## Passos para rodar o projeto:

1. Inicializar um ambiente virtual:
 ```shell 
virtualenv venv
```

2. Inicializar a sessão do terminal no ambiente virtual:
```shell
 source venv/bin/activate ou source bin/scripts/Activate
```

3. Instalar as dependências necessárias: 
``` shell
pip install -r requirements.txt
```

4. Iniciar o servidor Flask:
``` shell
 flask --app app.py run
```

### Servidor Flask
- O servidor será levantado na porta 5000 e conta com um único endpoint POST em /consulta/{cpf}. Onde é informado o cpf a ser consultado na url e passadas as informações de login como json no corpo da requisição no seguinte formato:
```json
{
    "login": string,
    "senha": string
}
```

- O retorno será um array de dados com os números dos benefícios daquele