'''Faça um programa que leia um número
qualquer e mostre seu fatorial.'''
#5x4x3x2x1
from math import factorial
numero = int(input('Digite um número:'))
fatorial = factorial(numero)
print(f' O fatorail de {numero}! é {fatorial}')

