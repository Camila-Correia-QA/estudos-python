'''Crie um programa que leia nome, ano de nascimento
e carteira de trabalho e cadastre-os
(com idade) em um dicionário se por acaso a CTPS
for diferente de zero, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

dados = dict()

dados['pessoa'] = input('Digite seu nome: ')
ano = int(input('Digite ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Digite sua CTPS: '))

if dados['ctps'] == 0:

    print(dados)
    print(f" Nome = {dados['pessoa']}")
    print(f" Idade = {dados['idade']}")
    print('O usuário não possui carteira de trabalho assinada!')
    exit()

else:

    dados['contratação'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Digite seu salário: '))
    print(dados)


print(f" Nome = {dados['pessoa']}")
print(f" Idade = {dados['idade']}")
print(f" CTPS = {dados['ctps']}")
print(f" Ano de contratação = {dados['contratação']}")
print(f" Salário = {dados['salario']}")
aposentadoria = dados['idade'] +((dados['contratação'] + 35) - datetime.now().year )

print(f" {dados['pessoa']} vai se aposentar com {aposentadoria} ")

#posentadoria = idade + 35 anos contratação
