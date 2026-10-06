'''Crie um programa onde o usuário possa digitar cinco
valores numéricos e cadastre-os em uma lista.
Já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
lista_de_numeros = []
for n in range(0,5):
    numero = int(input('Digite um número:'))
    lista_de_numeros.append(numero)
if numero:
    lista_de_numeros.index(numero)
print(lista_de_numeros)

