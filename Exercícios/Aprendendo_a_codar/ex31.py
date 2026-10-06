#Crie um programa que leia o ano de nascimento de sete
#pessoas.No final, mostra quantas pessoas ainda não atigiram
#a maioridade e quantas já são maiores

maior_de_idade = 0
menor_de_idade = 0
for c in range(1,8):
    numero = int(input('Digite um valor:'))
    if 2024 - numero < 18:
        menor_de_idade = menor_de_idade + 1

    else:
        maior_de_idade = maior_de_idade + 1

print(f'A quantidade de pessoas de menores de idade são {menor_de_idade}')
print(f'A quantidade de pessoas de maiores de idade são {maior_de_idade}')