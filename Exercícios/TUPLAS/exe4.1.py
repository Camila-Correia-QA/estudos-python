'''Crie um programa que vai gera cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que
estão na tupla'''
import random
tupla = tuple(random.randint(0, 100) for _ in range(5))
menor_numero = 100
maior_numero = 0
print(tupla)
for i in tupla:
    if i < menor_numero:
        menor_numero = i
    if i > maior_numero:
        maior_numero = i

print(f'O menor valor é {menor_numero}')
print(f' O maior valor é {maior_numero} ')




