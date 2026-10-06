'''Crie um programa onde o usuário digite uma
expressão qualquer que use parênteses.Seu aplicativo
deverá analisar se a expressão passada está com os parenteses
abertos e fechados na ordem correta.'''
cont_parenteses = 0

lista = input('Digite sua expressão: ')

for c in lista:

    if c == '(':
        cont_parenteses += 1

    elif c == ')':
        cont_parenteses -= 1

    if cont_parenteses < 0:
        break

if cont_parenteses == 0:
    print('Essa expressão é válida')

else:
    print('Essa expressão não é válida')
