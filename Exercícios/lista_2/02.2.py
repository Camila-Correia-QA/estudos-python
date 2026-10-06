'''Crie um programa onde o usuário possa digitar sete valores
númericos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares.No final, mostre os
valores pares e ímpares em ordem crescente'''

pares = []
impar = []
for c in range(0,7):
    number = int(input('Digite um número: '))
    if number %2 == 0:
        pares.append(number)
    else:
        impar.append(number)


print(f' A lista dos valores pares é {sorted(pares)}')
print(f' A lista dos valores ímpares é {sorted(impar)}')


