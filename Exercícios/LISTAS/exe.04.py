''' Crie um programa que vai ler vários números
e colocar em uma lista.
depois disso mostre:
a) quantos números foram digitados
b)A lista de valores, ordenada de forma DESCRESCENTE.
c)Se o valor 5 foi digitado e está ou não na lista.'''
numeros = []

continuar = 'S' or 'N'

while continuar == 'S':
    numero = int(input('Digite um número:'))
    numeros.append(numero)
    continuar = input('Deseja continuar ?').upper()
    if continuar != 'S':
        break
print(f' A lista tem {len(numeros)}')
print(sorted(numeros,reverse=True))
if 5 in numeros:
    print('Foi digitado o número 5')
else:
    print('Não existe o valor 5 na lista')
