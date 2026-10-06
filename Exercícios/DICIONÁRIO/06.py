'''Crie um programa que leia nome, sexo e idade
de várias pessoas, guardando os dados de cada pessoa
num dicionário e todos os dicionários em uma lista.No final,
mostre:
a)quantas pessoas foram cadastradas
b)a média de idade do grupo
c)uma lista com todas as mulheres.
d)uma lista com todas as pessoas com idade
acima da média.'''

pessoas = []
total_idade = 0
mulheres = []

continuar = 'S' or 'N'

while continuar == 'S':
    dados = dict()
    dados['Nome'] = input('Digite seu nome: ').title()
    dados['Gênero'] = input('Digite seu gênero M / F:').upper().strip()

    while dados['Gênero'] != 'M' and dados['Gênero'] != 'F':

        print('Esse gênero não existe, favor coloque corretamente!')
        dados['Gênero'] = input('Digite seu gênero M / F:').upper().strip()
    dados['idade'] = ''

    while not dados['idade'].isdigit():
        dados['idade'] = input('Digite sua idade: ')
    dados['idade'] = int(dados['idade'])
    pessoas.append(dados)
    if dados['Gênero'] == 'F':
        mulheres.append(dados['Nome'])
    continuar = input('Quer continuar? S/N').upper()
for pessoa in pessoas:
    total_idade += int(pessoa['idade'])

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade é {total_idade / len(pessoas)}')
print(f'As mulheres cadastradas foram:  {" ".join(mulheres)}')

media_idade = total_idade / len(pessoas)
pessoas_acima_media = [p['Nome'] for p in pessoas if p['idade'] > media_idade]
print(f' As pessoas com idade acima da média são {", ".join(pessoas_acima_media)}')
