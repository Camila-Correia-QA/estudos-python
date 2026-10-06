'''Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista.No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas
posições na lista.'''
numbers = []
for cont in range(0,5):
    numbers.append(int(input('Write an inter number:')))
print(f'O maior valor é {max(numbers)} que está na posição {numbers.index(max(numbers))} ')
print(f'o menor valor é {min(numbers)} que se encontra na posição {numbers.index(min(numbers))}')
print(numbers)