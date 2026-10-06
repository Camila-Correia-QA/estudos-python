'''Faça um programa que leia 5 valores numéricos e
guarde-os em uma lista.No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas
posições na lista.'''
#c = posição na lista
#v = valor nessa posição
numbers = []
more = 0
less = 1000
position_more = 0
position_less = 0
for cont in range(0,5):
    number = int(input('Write a inter number:'))
    numbers.append(number)
for position, number in enumerate(numbers):
    if number > more :
        more = number
        position_more = position
    if number < less:
        less = number
        position_less = position
print(f' The list of the numbers are: {numbers}')
print(f' The biggest number is {more} and found in position {position_more+1}')
print(f' The smallest number is {less} and found in position {position_less+1}')

