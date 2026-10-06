'''Crie um programa que vai gera cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que
estão na tupla'''
import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
e = random.randint(0,9)
f = random.randint(0,9)

lista = (a, b, c, d, e,f)
print(f'Os valores sorteador foram: {lista}')
print(f'{min(lista)} é o menor número!')
print(f'{max(lista)} é o maior número!')






