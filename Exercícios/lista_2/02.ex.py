'''Faça um programa que leia nome e peso de
várias pessoas, guardando tudo em uma lista.
No final, mostre:
 a) quantas pessoas foram cadastradas
 b)uma listagem com as pessoas mais pesadas
 c)uma listagem com as pessoas mais leves'''

pessoas = []

pessoas_leve = []

pessoas_pesadas = []

continuar = 'S' or 'N'

while continuar == 'S':
    dados = []
    nome = input('Digite um nome: ')
    peso = int(input('Digite um peso:'))
    dados = [nome,peso]
    pessoas.append(dados[:])

    if peso <= 50:
        pessoas_leve.append(dados)

    elif peso >= 100:
        pessoas_pesadas.append(dados)

    #dados.clear()
    continuar = input('Deseja continuar? S/N').upper()

print(f'Foram cadastradas {len(pessoas)} pessoas no sistema!')
print(f'Pessoas acima do peso {pessoas_pesadas}')
print(f'Pessoas abaixo do peso {pessoas_leve}')









