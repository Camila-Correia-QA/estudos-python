#Desenvolva um programa que leia o primeiro termo
#E a razão de uma PA.No final, mostre os 10 primeiros termos
#Dessa progressão.
#pa = a1 + (n-1).r
a1 = int(input('Digite um valor:'))
r = int(input('Digite outro valor:'))
for n in range(10):
    pa = a1 + n * r
    print(pa)

