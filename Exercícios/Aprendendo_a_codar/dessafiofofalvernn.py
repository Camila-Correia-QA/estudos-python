'''Temos a Lista [1,7,9,10,6]


-13
 - 16 - 17 - 13
11- 17- 19- 16
- 13 - 15 -16

Vc dará a entrada de um numero inteiro.

Se esse numero for igual a soma de dois numeros da lista a resposta é True
Caso não for é False

numero = int(input('Escolha um número: '))

if (numero == 7 or numero == 8 or numero == 10 or numero == 11 or numero == 13
    or numero == 15 or numero == 16 or numero == 17 or numero == 19):
    print('ESSE NÚMERO É VERDADEIRO!')
else:
    print('ESSE NÚMERO É FALSO!!')'''

lista = []
continuar = 'S'
while continuar == 'S':
    number = int(input('Digite um número: '))
    lista.append(number)
continuar = (' Deseja continuar? S / N: ').upper()
break