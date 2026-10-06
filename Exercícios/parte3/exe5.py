'''Faça um programa que leia um número
qualquer e mostre seu fatorial.'''
#5x4x3x2x1
numero = int(input('Digite um número:'))
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1
print(f'O fatorial é {fatorial}')
