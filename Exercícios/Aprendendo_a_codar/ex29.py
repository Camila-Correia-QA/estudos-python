#Faça um programa que leia um número inteiro
#E diga se ele é ou não um número primo
numero = int(input('Digite um número inteiro:'))
isprime = True
for c in range(2, numero):
    if numero %c == 0:
        isprime = False
if isprime:
    print('O número é primo')
else:
    print('O Número não é primo')
