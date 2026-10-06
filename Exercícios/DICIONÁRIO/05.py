'''Crie um programa que gerencia o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida.No final, tudo isso será guardado em um dicionário, incluindo gols
feitos durante o campeonato.'''

dados = dict()
dados['Jogador'] = input('Digite o nome do jogador: ')
dados['Partidas'] = int(input('Quantas partidas jogou?: '))
gol = []
if dados['Partidas'] <= 0:
    print(dados)
    print('Não existe essa possibilidade')
    exit()
else:
    for c in range(dados['Partidas']):
        gols = int(input(f'Quantos gols fez na partida {c +1}?'))
        if gols >=0:
            gol.append(gols)
            dados['Gols'] = (sum(gol))
            dados['Ordem dos gols'] = gol
        else:
            print(dados)
            print('Não existe essa possibilidade.')
            exit()

print('--------------------------')
print(dados)
print('--------------------------')
print(f"Nome do jogador: {dados['Jogador']}")
print(f"Lista dos gols: {dados['Ordem dos gols']}")
print(f"Total de gols: {sum(gol)} gols!")
print('--------------------------')
print(f"O jogador {dados['Jogador']} jogou {dados['Partidas']} partidas.")
for k in range(dados['Partidas']):
    print(f'Na partida {k+1} , fez {gol[k]} gols')
print(f'Foi um total de {sum(gol)} gols!')
