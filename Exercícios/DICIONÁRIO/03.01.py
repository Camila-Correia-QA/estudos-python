import random
from time import sleep

jogador = {}

for c in range (0,4):
    chave = f'jogador {c +1}'
    jogador[chave] = random.randint(1, 6)
    print(f' O jogador {c + 1} tirou {jogador [chave]} \n')
    sleep(1)
print('------ RANKING DOS JOGADORES ------')
for k in range (6,0,-1):
    for c in range(0,4):
        chave = f'jogador {c + 1}'
        if jogador[chave] == k:
            print(f'O xº LUGAR {chave} tirou {k}')


