'''Faça um programa que tenha uma lista chamada
números e duas funções
chamadas sorteia() e soma_par().
A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos
os valores PARES sorteados pela função anterior'''

import random

lista = []

def sorteia():
    for s in range(5):
        s = random.randint(0,100)
        lista.append(s)
        print(s)
    print(lista)
    pares(lista)

def pares(lista):
    pares = []
    for l in lista:
        if l % 2 == 0:
            pares.append(l)
    print(sum(pares))
    print(pares)



sorteia()
