"""Crie um programa que leia 2 valores e
mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa"""
valor1 = int(input('Digite um valor:'))
valor2 = int(input('Digite mais um valor:'))
valores = []
valores.append(valor1)
valores.append(valor2)
print('Escolha uma opção')
print('[1] para somar')
print('[2] multiplicar')
print('[3] maior')
print('[4]novos números')
print('[5]sair do programa')
opcao = int(input('Digite uma opção:'))
while opcao != 5:
    if opcao == 1:
        print(f'A soma é { valor1 + valor2 } ')
        opcao = int(input('Digite uma opção:'))
    if opcao == 2:
        print(f'{valor1 * valor2}')
        opcao = int(input('Digite uma opção:'))
    if opcao == 3:
        print( f'O número {max(valores)} é o maior número.')
        opcao = int(input('Digite uma opção:'))
    if opcao == 4:
        valor1 = int(input('Digite um valor:'))
        valor2 = int(input('Digite mais um valor:'))
        opcao = int(input('Digite uma opção:'))
        valores.append(valor1)
        valores.append(valor2)

print('VOCÊ SAIU DO PROGRAMA!')
