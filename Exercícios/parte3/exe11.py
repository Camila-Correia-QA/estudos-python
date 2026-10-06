'''Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário digitar o valor
999. Que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles , desconsiderando o flag'''
numero = int(input('Digite um valor: '))
n = 0
soma_n = 0
while numero != 999:
    n += 1
    soma_n += numero
    numero = int(input('Digite um valor: '))


print(f'Foram digitados {n} números com soma de {soma_n} ')