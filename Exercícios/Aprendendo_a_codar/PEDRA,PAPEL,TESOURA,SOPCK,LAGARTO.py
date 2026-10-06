import random

from time import sleep

game = ['pedra', 'papel', 'tesoura', 'spock', 'lagarto']

jogada = input('Jogue PEDRA, PAPEL, TESOURA, LAGARTO OU SPOCK: ').strip().lower()
while (jogada != 'pedra'
       and jogada != 'papel'
       and jogada != 'tesoura'
       and jogada != 'spock'
       and jogada != 'lagarto'):
    print('tente novamente: ')
    jogada = input('Jogue PEDRA, PAPEL, TESOURA, LAGARTO OU SPOCK: ').strip().lower()

print('PEDRA')

sleep(1)

print ('PAPEL')

sleep(1)

print('TESOURA')

sleep(1)

print('LAGARTO')

sleep(1)

print('SPOCK')

sleep(1)

print('...')

sleep(1)

computador_escolhe = (random.choice(game))
#computador_escolhe = input('Digite PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK: ').strip().lower()
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
spock = 'spock'
lagarto = 'lagarto'

if jogada == computador_escolhe:
    print('O JOGO DEU EMPATE!!! ')
    quit()

if jogada == pedra:

    if computador_escolhe == papel:
        print('PERDEU!! VOCÊ FOI EMBRULHADO COM UM LIXO MUAHAHAHA !!! ')

    elif computador_escolhe == tesoura:
        print('PARABÉNS! VOCÊ APEDREJOU SEU INIMIGO!!')

    elif computador_escolhe == lagarto:
        print('PARABÉNS!! VOCÊ ESMAGOU O LAGARTO!!!')

    elif computador_escolhe == spock:
        print('MAIS UMA DERROTA!! VOCÊ FOI EVAPORADO!!!')

elif jogada == papel:

    if computador_escolhe == pedra:
        print('ARRASOU!!! VOCÊ EMBRULHOU SEU INIMIGO COMO LIXO !! MUAHAHAH')

    elif computador_escolhe == tesoura:
        print('CORTE TRAMONTINA!! VOCÊ FOI PICOTADINHO')

    elif computador_escolhe == lagarto:
        print('QUE PENA!!! FOI DE BASE! VOCÊ FOI DEVORADO PELO LAGARTO')

    elif computador_escolhe == spock:
        print('PARABÉNS VOCê DETONOU SEU INIMIGO MUAHHAHAHA!!')

elif jogada == tesoura:

    if computador_escolhe == pedra:
        print('SUA TESOURA FOI DESTRUÍDA COM UM PEDRADA T.T ')

    elif computador_escolhe == papel:
        print('PARABÉNS! VOCÊ PICOTOU SEU INIMIGO!!! ')

    elif computador_escolhe == lagarto:
        print('VOCÊ PICOTOU SEU INIMIGO !! MUAHAHAH')

    elif computador_escolhe == spock:
        print('QUE PENA!! SUA TESOURA FOI DERRETIDA!!  ')

elif jogada == lagarto:

    if computador_escolhe == pedra:
        print('QUE PENA!! VOCÊ FOI ESMAGADO COM UMA PEDRADA!!')

    elif computador_escolhe == papel:
        print('QUE DELÍCIA VOCÊ ACABA DE DEVORAR UM PAPEL!!!')

    elif computador_escolhe == tesoura:
        print('QUE PENA VOCÊ FOI PICOTADO POR SEU INIMIGO!!')

    else:
        print('PARABÉNS VOCÊ ENVENENOU SEU INIMIGO')

elif jogada == spock:

    if computador_escolhe == pedra:
        print('PARABÉNS VOCÊ VAPORIZOU SEU INIMIGO!! ')

    elif computador_escolhe == papel:
        print('QUE PENA VOCÊ FOI REFUTADO!!')

    elif computador_escolhe == tesoura:
        print('VOCÊ DERRETEU SEU INIMIGO MUHHAHAH!!!')

    else:
        print('VOCÊ FOI DE BASE E ARRASTOU PARA CIMA COM O VENENO DO LAGARTO!!')

print(f' Você escolheu {jogada} e seu inimigo {computador_escolhe}!! ')

