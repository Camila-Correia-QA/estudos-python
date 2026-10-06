soma = 0
cont = 0
for c in range (1,501):
    if c% 3 == 0 and c% 2 != 0:
        soma = soma + c
        cont = cont + 1
        print(c)
print(f'A soma dos números ímpares e múltiplos de três é {soma} no total de {cont} números.')

