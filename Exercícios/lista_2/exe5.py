'''Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.'''
import random

mega_sena = []

for s in range(1,61):
    mega_sena.append(s)

quantidade_jogos = int(input('Quantos jogos da mega sena deseja realizar?: '))

for c in range(quantidade_jogos):
    print(f'Jogo {c+1}:', random.sample(mega_sena, k = 6))
print('Fim! Boa Sorte!')
