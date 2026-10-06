'''Crie um programa onde 4 jogadores
joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número
no dado.'''

import random
from time import sleep
players = dict()
jogadas = list()
maior_jogador = []

for c in range(0,4):
    players['jogada'] = random.randint(1,6)
    print(f' O jogador {c+1} tirou {players["jogada"]} \n')
    sleep(1)
    jogadas.append(players.copy())
    len(players) > 1

print('Ranking dos jogadores: ')
print(jogadas)
print(maior_jogador)