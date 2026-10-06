'''Crie uma tupla preenchida com os 20 primeiros
colocados da tabela do campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a)Apenas os 5 primeiros colocados.
b)Os últimos 4 colocados da tabela.
c)Uma lista com os times em ordem alfabética.
d)Em que posição na tabela está o time da Bahia.
'''
times_futebol = ('Corinthians', 'Flamengo', 'Vasco', 'Grêmio', 'Bahia', 'Botafogo', 'Fluminense',
                 'São Paulo', 'Atlético mineiro', 'Palmeiras')
print(f' Os 5 primeiros colocados são{times_futebol[0:5]}')
print('---'*50)
print(f' Os 4 últimos colocados da tabela são {times_futebol[-4:]}')
print('---'*50)
print(f' A lista em ordem alfabética fica {sorted(times_futebol)}')
print('---'*50)
print(f' A bahia se encontra na {times_futebol.index("Bahia")+1}ª Colocação')
