'''Desenvolva um programa que leia
quatro valores pelo teclado e guarde-os
em uma tupla. No final mostre:
a)Quantas vezes apareceu o valor 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.'''
valores = tuple(int(input('Digite um valor: '))for _ in range(4))
nove = 0
par = []
tres = -1
cont = 0
for i in valores:
    cont = cont + 1
    if i == 9:
        nove += 1
    if i %2  == 0:
        par.append(i)
    if i == 3 and tres == -1:
        tres = cont

if tres == -1:
    print('Não há 3 na tupla!')
else:
    print(f'O 3 se encontra na posição {tres}')

print(f'O valor 9 apareceu {nove} vezes')
print(f'Os números que são pares são {par}')
