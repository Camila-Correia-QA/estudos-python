'''Faça um programa que tenha uma função chamada
contador(), que recebe trÊs parâmetros: início, fim e passo e
realiza a contagem.
Seu programa tem que realizar três contagens através da função criada.
a)de 1 ate 10, de 1 em 1
b) de 10 té 0, de 2 em 2
c)uma contagem personalizada'''

from time import sleep

a = '-' * 30
def contador(i,m,f):
    if f == 0:
        f = -1
    for c in range(i,m,f):
        sleep(1)
        print(c)


contador(1,11,1)
print(a)
contador(10,0,-2)
print(a)
contador(10,101,10)
print(a)
print('FIM')

