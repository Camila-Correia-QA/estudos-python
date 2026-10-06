'''Faça um programa que tenha uma função chamada área()
,que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''

print('CONTROLE DE TERRENOS')
print('-' * 30 )
def area (b,h):
    a = b * h
    print(f' O comprimento do terreno de {b} x {h} será {a}')


b = float(input('Digite a largura: '))
h = float(input('Digite o coprimento: '))


area(b,h)




