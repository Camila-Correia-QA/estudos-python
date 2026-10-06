''' Crie um programa que vai ler vários números
e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar
apenas os valores pares e os valores ímpares, digitados
respectivamente.
ao final mostre o conteudo das três listas geradas.'''
lista_geral = []

lista_pares = []

lista_impares = []

continuar = 'S' or 'N'

while continuar == 'S':
    numero = int(input('Digite um número inteiro: '))
    lista_geral.append(numero)
    continuar = input('Deseja continuar? S/N').upper()
    if numero %2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    if continuar =='N':
        print(f' A lista principal é {lista_geral}')
        print(f' A lista dos números pares é {lista_pares}')
        print(f' A lista dos números ímpares é {lista_impares}')