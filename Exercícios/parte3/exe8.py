#Desenvolva um programa que leia o primeiro termo
#E a razão de uma PA.No final, mostre os 10 primeiros termos
#Dessa progressão. o programa encerra quando falar 0 termos
#pa = a1 + (n-1).r
a1 = int(input('Digite um valor:'))
r = int(input('Digite outro valor:'))
n = 0
limite = 10
i = 0
while i < limite:
	pa = a1 + n * r
	print(f'{pa}')
	n += 1
	i += 1
	if i >= limite:
		limite = int(input('Digite quantas vezes que repetir:'))
		i = 0

print('Fim da progressão aritmética!')

