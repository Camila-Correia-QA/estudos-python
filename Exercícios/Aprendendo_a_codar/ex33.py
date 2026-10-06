#Desenvolva um programa que leia o nome,idade e sexo de 4
#pessoas.No final do programa mostra:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
#média = idade + idade + idade + idade /4
idades = []
nomes = []
sexos = []
idade_mais_velha = 0
nome_mais_velho = ''
idades_mulheres_mais_velhas = []
for c in range(0,4):
    print( f' *** {c + 1}ª PESSOA ***')
    nome = input('Diga seu nome:')
    nomes.append(nome)
    idade = int(input('Digita sua idade:'))
    idades.append(idade)
    sexo = input('Digite seu sexo: masculino ou feminino:')
    sexos.append(sexo)
    print(f'{nome}')
    print(f'{idade}')
    print(f'{sexo}')
    if sexos[c] == 'm' and idades[c] > idade_mais_velha:
        idade_mais_velha = idades[c]
        nome_mais_velho = nomes[c]
    if sexos[c] == 'f' and idades[c] <= 20:
        idades_mulheres_mais_velhas.append(idade)

soma_idades = sum(idades)
media = soma_idades / 4
print(f'A média da idade das 4 pessoas é {media}')
print(f'O nome do homem mais velho é {nome_mais_velho} com {idade_mais_velha} anos')
print(f'A quantidade de mulheres mais velhas são {len(idades_mulheres_mais_velhas)}')





