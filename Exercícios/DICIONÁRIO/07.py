'''Crie um programa que gerencia o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida.No final, tudo isso será guardado em um dicionário, incluindo gols
feitos durante o campeonato.
-- Aprimore o desafio para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes
de aproveitamento de cada jogador.'''

lista_dicionario_jogadores = []
continuar = 'S'
while continuar == 'S':
    gol = []
    dados = dict()
    dados['Jogador'] = input('Digite o nome do jogador: ')
    dados['Partidas'] = int(input('Quantas partidas jogou?: '))
    if dados['Partidas'] <= 0:
        print(dados)
        print('Não existe essa possibilidade')
        exit()
    else:
        for c in range(dados['Partidas']):
            gols = int(input(f'Quantos gols fez na partida {c +1}?'))
            if gols >= 0:
                gol.append(gols)
                dados['Gols'] = (sum(gol))
                dados['Ordem dos gols'] = gol
            else:
                print(dados)
                print('Não existe essa possibilidade.')
                exit()
    lista_dicionario_jogadores.append(dados)

    continuar = input('Deseja continuar?: ').upper()

for dados in lista_dicionario_jogadores:
    print('-' * 30)  # Separador visual
    print(f"Nome do jogador: {dados['Jogador']}")
    print(f"Lista dos gols: {dados['Ordem dos gols']}")
    total_gols = sum(dados['Ordem dos gols'])
    print(f"Total de gols: {total_gols} gols")
print(f"O jogador {dados['Jogador']} jogou {dados['Partidas']} partidas.")

print(lista_dicionario_jogadores)
print('--------------------------')
for jogador in lista_dicionario_jogadores:
    print(f'{jogador}')