"""Melhore o jogo do desafio 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só  que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer."""
import random
num = (random.randint(1,10))
quantidade_number = []
numero = int(input('Adivinhe o número que estou pensando:'))
while numero != num:
    print('Tente outra vez, você errou!!!')
    numero = int(input('Adivinhe o número que estou pensando:'))
    quantidade_number.append(numero)
print(f'Parabéns você adivinhou o número {num} com {len(quantidade_number) +1} tentativas')


