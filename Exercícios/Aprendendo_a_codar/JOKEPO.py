import random
from time import sleep
jkp = ['pedra', 'papel', 'tesoura']
jogo = (input('Jogue! Pedra, papel ou tesoura:').lower())
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('...')
computador_joga = (random.choice(jkp))
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
print(f'o computador jogou {computador_joga}')

if computador_joga == jogo:
    print('Empate de jogo!!')

#pedra vence tesoura
elif computador_joga == pedra and jogo == tesoura:
    print('Que pena, você tomou uma pedrada!!! ')

#pedra perde pra papel
elif computador_joga == pedra and jogo == papel:
    print('Parabéns você venceu na base do amasso!! ')

#papel ganha de pedra
elif computador_joga == papel and jogo == pedra:
    print('Que pena, você foi embrulhado como um lixo!!!')

#papel perde para tesoura
elif computador_joga == papel and jogo == tesoura:
    print('Parabéns você fatiou seu inimigo!!! MUAHAAHAHAHA')

#tesoura ganha para papel
elif computador_joga == tesoura and jogo == papel:
    print('Que pena, tramontina corte rápido, você foi picotado !!!! ')

#tesoura perde para pedra
elif computador_joga == tesoura and jogo == pedra:
    print('Parabéns você venceu coloca o capacete que lá vem pedrada!!!')








