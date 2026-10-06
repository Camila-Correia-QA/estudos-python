#Crie o jogo da velha:
def imprime_tabuleiro (tabuleiro):
    for linha in tabuleiro:
        for coluna in linha:
            print(coluna, end=' ')
        print('')

def vitoria(jogador,tabuleiro):
    trio = [jogador,jogador, jogador]
    if tabuleiro[0] == trio or tabuleiro[1] == trio or tabuleiro[2] == trio:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][0] == jogador and tabuleiro[2][0] == jogador:
        return True

    if tabuleiro[0][1] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][1] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

#imprime_tabuleiro([['x','o','o'],['x','o','x'],['x','o','x']])
tabuleiro = [['-','-','-'], ['-', '-', '-'], ['-', '-', '-']]
jogadas = 0
jogador_x = 'x'
jogador_o = 'o'
jogador = jogador_o
while jogadas != 9:
    x = input('Qual linha você deseja?')
    if x != '0' and x != '1' and x != '2':
        print('Digite um valor dentro da matriz seu burro!')
        continue
    y = input('Qual coluna você deseja?')
    if y != '0' and y != '1' and y != '2':
        print('Digite um valor dentro da matriz seu burro!')
        continue
    if tabuleiro[int(x)][int(y)] != '-':
        print('Esse lugar já está ocupado!')
        continue
    tabuleiro[int(x)][int(y)] = jogador
    imprime_tabuleiro(tabuleiro)
    if vitoria(jogador, tabuleiro):
        print(f'Jogador {jogador} ganhou!!')
        print('Game Over!!')
        break
    jogadas += 1
    if jogador == 'o':
        jogador = jogador_x
    else:
        jogador = jogador_o
else:
    print('Deu empate!!!')

#(f'\33[7;30;43m{nome}\33[m')

# diagonal[0,0][1,1][2,2]
#diagonal [0,2][1,1][2,0]
#colunas [0,0][1,0][2,0]
#colunas1 [0,1][1,1][2,1]
#colunas2 [0,2][1,2][2,2]





