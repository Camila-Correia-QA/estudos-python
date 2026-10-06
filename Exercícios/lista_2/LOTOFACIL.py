import random

lotofacil = []

for s in range(1,26):
    lotofacil.append(s)

quantidade_jogos = int(input('Quantos jogos da lotofácil deseja realizar?: '))

for c in range(quantidade_jogos):
    print(f'Jogo {c+1}:', random.sample(lotofacil, k = 15))
print(' Os números da lotofácil foram:', random.sample(lotofacil, k = 15))
print('Fim! Boa Sorte!')
