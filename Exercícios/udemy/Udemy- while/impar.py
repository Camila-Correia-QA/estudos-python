'''Calcule a soma dos números ímpares entre eles.'''
x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
soma = 0
if x > y:
    for c in range (y,x):
        if c % 2 != 0:
            soma += c
            print(f' {c}')
    print(f' A soma dos números ímpares são {soma}')

else:
    for c in range(x,y):
        if c % 2 !=  0:
            soma += c
            print(f' {c} ')
    print(f' A soma dos números ímpares são {soma}')



