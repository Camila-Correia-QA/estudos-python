'''Faça um programa que mostra a tabuda de vários números, um de cada
vez, para cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.'''
numero = int(input('Digite um número:'))
while True:
    if numero > 0:
        print(f'A tabuada de {numero} é:')
    for n in range (1,11):
        print(f' {numero} x {n} = {numero * n}')
    numero = int(input('Digite um número: '))
    if numero <0:
        print('PROGRAMA DA TABUADA ENCERRADO, VOLTE SEMPRE!')
        break
