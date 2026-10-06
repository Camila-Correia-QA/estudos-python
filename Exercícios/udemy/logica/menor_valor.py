valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite um número: '))
valor_3 = int(input('Digite um número: '))
menor_valor = 100

if valor_1 < 100:
    menor_valor = valor_1
if valor_2 < valor_1:
    menor_valor = valor_2
if valor_3 < valor_2:
    menor_valor = valor_3

print(f'O menor valor é {menor_valor}')