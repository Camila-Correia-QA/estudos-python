'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar  quando o usuário digitar o valor 999, que é a
condição de parada.No final, mostre qantos números foram
digitador e qual f a soma entre .'''
numero = int(input('Digite um número: '))
cont = 0
soma = 0
while True:
    cont += 1
    soma += numero
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
print(f'foram digitados {cont} números e a soma deles é {soma} ')

