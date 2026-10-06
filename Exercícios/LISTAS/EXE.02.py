'''Crie um programa onde o usuário possa digitar
vários valores numéricos e cadasre-os em uma
lista. Caso o número já exista lá dentro, ele
não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
'''
numbers = []

continuar = 'Y' or 'N'

while continuar == 'Y':
        number = int(input('Write a inter number: '))
        continuar = input('Do you want to continue?: Y/N').upper()

        if number not in numbers:
            numbers.append(number)

        if continuar == 'N':
            print(f'The order the of numbers are: {sorted(numbers)}')



