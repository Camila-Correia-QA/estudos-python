def exibe(jogo):
    for x in range(0, 3):
        for y in range(0, 3):
            print(jogo[x * 3 + y], end=" ")
        print()


casos_vitoria = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def verifica_vitoria(jogo, j):
    for pos in casos_vitoria:
        if jogo[pos[0]] == j and jogo[pos[1]] == j and jogo[pos[2]] == j:
            return True
    return False


def digite(p):
    while True:
        j = input(f'Em que {p} deseja jogar (0, 1 ou 2): ')
        if j != '0' and j != '1' and j != '2':
            print('Opção inválida. Tente novamente.')
            continue
        return int(j)


def jogada(jogo, x, y, j):
    p = x * 3 + y
    if jogo[p] != '-':
        print('Jogada inválida')
        return
    jogo[p] = j


jogo = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
jogador, proximo_jogador = 'x', 'o'

while '-' in jogo:
    exibe(jogo)
    x = digite('linha')
    y = digite('coluna')
    jogada(jogo, x, y, jogador)
    if verifica_vitoria(jogo, jogador):
        print(f'Jogador {jogador} vence o jogo')
        break
    jogador, proximo_jogador = proximo_jogador, jogador
else:
    print("Deu Velha!")

print("Fim de jogo")

