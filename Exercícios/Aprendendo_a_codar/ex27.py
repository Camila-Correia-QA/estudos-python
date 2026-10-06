"""Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.Se
o valor for ímpar,desconsidere-se"""
numeros_pares = []
soma = 0
cont = 0
for c in range(0,6):
    numero = int(input('Digite um valor:'))
    if numero % 2 == 0:
        soma += numero
        cont += 1
        numeros_pares.append(numero)
print(numeros_pares)
print(sum(numeros_pares))
print(f' Você informou {cont} números PARES e a soma deles é igual a {sum(numeros_pares)}')



