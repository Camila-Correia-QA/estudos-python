'''Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.'''

def texto():
    txt = input('Digite uma frase: \n')
    a = '-' * len(txt)
    print(a)
    print(txt)
    print(a)


texto()

