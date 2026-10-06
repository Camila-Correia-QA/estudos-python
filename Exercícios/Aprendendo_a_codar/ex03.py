velocidade = float(input('Digite a velocidade do carro:'))
multa = (velocidade - 80)*7
if velocidade > 80:
    print(f'Você recebeu uma multa no valor de {multa}.')
else:
    print(f'Você está dentro do limite de velocidade')
print('Tenha um bom dia! Dirija com segurança!')