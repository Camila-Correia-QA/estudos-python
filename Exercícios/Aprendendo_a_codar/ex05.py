distancia_viagem = float(input('Qual a distância da viagem?'))
valor_viagem_curta = 0.50 * distancia_viagem
valor_viagem_longa = 0.45 * distancia_viagem
if distancia_viagem <= 200:
    print(f' A passagem custará {valor_viagem_curta}')
else:
    print(f' A passagem custará {valor_viagem_longa}')