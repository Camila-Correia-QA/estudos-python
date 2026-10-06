pessoas = []
total_idade = 0
mulheres = []

continuar = 'S'

while continuar == 'S':
    dados = {}  # Reinicializa o dicionário a cada iteração
    dados['Nome'] = input('Digite seu nome: ').title()
    dados['Gênero'] = input('Digite seu gênero M / F: ').upper()

    while dados['Gênero'] != 'M' and dados['Gênero'] != 'F':
        print('Esse gênero não existe, favor coloque corretamente!')
        dados['Gênero'] = input('Digite seu gênero M / F: ').upper()

    dados['idade'] = input('Digite sua idade: ')
    while not dados['idade'].isdigit():
        print('Idade inválida! Por favor, insira um número.')
        dados['idade'] = input('Digite sua idade: ')

    dados['idade'] = int(dados['idade'])  # Converte a idade para inteiro
    pessoas.append(dados)

    if dados['Gênero'] == 'F':
        mulheres.append(dados['Nome'])

    total_idade += dados['idade']

    continuar = input('Quer continuar? S/N ').upper()

# Cálculo da média de idade
media_idade = total_idade / len(pessoas)

# Mostrar resultados
print(f'\nForam cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade do grupo é {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: {", ".join(mulheres)}')

# Pessoas com idade acima da média
pessoas_acima_media = [p['Nome'] for p in pessoas if p['idade'] > media_idade]
print(f'As pessoas com idade acima da média são: {", ".join(pessoas_acima_media)}')