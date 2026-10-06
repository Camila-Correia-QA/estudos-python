''' Escreva um programa que leia um número n
inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de fibonacci'''
#Ler número n
numero = int(input('Digite um número: '))
indice = 0
p1 = 0
p2 = 1
print(f' A sequência de fibonacci é :')
while indice < numero:
    p3 = p1 + p2
    p1 = p2
    p2 = p3
    print(f'{p3}')
    indice += 1
print('Sequência finalizada.')
# 1- 1 - 2 - 3 - 5 - 8- 13 - 21 - 34
# Fn = fn-1 + Fn-2, sendo o primeiro termo F1= 1 e os valores iniciais F1 = 1, F2 =1.

