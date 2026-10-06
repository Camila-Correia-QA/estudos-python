'''Crie um programa que crie uma matriz
de dimensão 3x3 e preencha com valores
lidos pelo teclado, no final mostre a
 matriz na tela, com a formatação
correta.'''

matriz = []

for m in range (3):
    numero = []
    for c in range (3):
        number = int(input(f'Digite um número na posição [{m+1}],[{c+1}]: '))
        numero.append(number)
    matriz.append(numero)
for linha in matriz:
    print(" ".join(f"[{valor}]" for valor in linha))


