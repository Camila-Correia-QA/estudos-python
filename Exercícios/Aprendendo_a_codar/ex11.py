import math
nome = input('Digite seu nome:')
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
quantos_anos = int(input('Em quantos anos pretende pagar?'))
parcela= quantos_anos * 12
prestacao = valor_casa / parcela
print(f'{prestacao}')
print(f'{parcela}')
if prestacao > 0.30*salario:
    print('Infelizmente, seu empréstimo foi negado')
else:
    print(f'PARABÉNS {nome}! O seu empréstimo foi APROVADO com {parcela} parcelas de R$ {prestacao}!!')