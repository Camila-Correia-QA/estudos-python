#Faça um programa que leia o peso de cinco pessoas.
#no final, mostre qual foi o maior e o menor peso lidos.
pesos = []
for c in range(1,6):
    peso = float(input('Digite o peso:'))
    pesos.append(peso)
peso_minimo = min(pesos)
peso_maximo = max(pesos)
print(f'O peso maior é {peso_maximo}')
print(f'O peso menor é {peso_minimo}')




