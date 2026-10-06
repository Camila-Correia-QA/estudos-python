print('-----BANCO DA MILOUCA-------')
dinheiro = int(input('Quanto você quer sacar? '))
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
cedulas_1 = 0
dinheiro_1 = dinheiro
while dinheiro > 0:
  if dinheiro >= 50:
    cedulas_50 += 1
    dinheiro -= 50
  elif dinheiro >= 20:
    cedulas_20 += 1
    dinheiro -= 20
  elif dinheiro >= 10:
    cedulas_10 += 1
    dinheiro -= 10
  else:
    cedulas_1 = dinheiro
    dinheiro = 0

print(f'Você terá um saque de R$  {dinheiro_1} com:')
print(f'{cedulas_50} cédulas de R$ 50')
print(f'{cedulas_20} cédulas de R$ 20')
print(f'{cedulas_10} cédulas de R$ 10')
print(f'{cedulas_1} cédulas de R$ 1')