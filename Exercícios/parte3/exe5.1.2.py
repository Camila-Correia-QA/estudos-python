'''Faça um programa que leia um número
qualquer e mostre seu fatorial.'''
#5x4x3x2x1
n = int(input('Digite um número para calcular seu fatorial'))
c = n
f = 1
while c > 0:
    print(f'{c}', end ='')
    print('x' if c > 1 else ' = ', end='')
    f *=c
    c -=1
print(f'O fatorial de {n}! é {f}')