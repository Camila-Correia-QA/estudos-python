'''Aprimore o desafio anterior, mostrando no final:
A)A soma de todos os valores pares digitados.
B)A soma dos valores da terceira coluna
C)O maior valor da segunda linha'''

matriz = []
pares = 0
coluna = 0
for m in range (3):
    numero = []
    for c in range (3):
        number = int(input(f'Digite um número na posição [{m+1}],[{c+1}]: '))
        numero.append(number)
        if number %2 == 0:
            pares += number
    matriz.append(numero)
for linha in matriz:
    coluna += linha[2]
maior_numero = 0
for col in matriz[1]:
    if col > maior_numero:
        maior_numero = col
print(f'O maior número da linha 2 é {maior_numero}' )
print(f'A soma da terceira coluna é : {coluna}!')
print(f'A soma de todos os valores pares é {pares}')
for linha in matriz:
    print(" ".join(f"[{valor}]" for valor in linha))


