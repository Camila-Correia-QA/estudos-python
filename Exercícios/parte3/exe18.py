'''Crie um programa que leia o nome e o preço de
vários produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c)Qual é o nome do produto mais barato.'''
print('-----LOJA MILOUCAX-----')
lista_de_produtos = []
lista_de_precos = []
soma = 0
mais_de_mil = 0
continuar = 'S'
produto_mais_barato = ''
preco_mais_barato = 999999

while continuar == 'S':
    produto = input('Digite o nome do produto: ')
    lista_de_produtos.append(produto)
    preco = int(input('Digite o preço'))
    lista_de_precos.append(preco)
    soma += preco
    if preco > 1000:
        mais_de_mil += 1
    continuar = input('Deseja continuar? S / N:').upper()
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = produto

    if continuar == 'N':
        break
print(f'O total de gasto de compras foi {soma}')
print(f'Existem {mais_de_mil} produtos que valem mais de R$1000,00')
print(f'O produto mais barato é {produto_mais_barato} e custa R${min(lista_de_precos)}')



