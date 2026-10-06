import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]
print(cotacoes)
print(cotacao_dolar)
