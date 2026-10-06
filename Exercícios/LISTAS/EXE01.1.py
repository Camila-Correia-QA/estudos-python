'''Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista.No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas
posições na lista.'''
numbers = []

the_biggest_number = 0

the_less_number = 100

for cont in range(0,5):
    number = (int(input('Write an inter number ')))
    numbers.append(number)

    if number < the_less_number:
        the_less_number = number

    elif number > the_biggest_number:
        the_biggest_number = number

print(f'{numbers}')
print(f'O maior número {the_biggest_number} se encontra na posição {numbers.index(the_biggest_number)+1}')
print(f'O menor número {the_less_number} se encontra na posição {numbers.index(the_less_number)+1}')

