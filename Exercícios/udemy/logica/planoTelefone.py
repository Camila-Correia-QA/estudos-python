plano = 50
minutos = 100
p = int(input('Digite quantos minutos você gastou: '))
if p <= 100:
    print('Esse mês seu plano sairá por R$ 50,00 ')
else:
    print(f'Esse mês seu plano sairá por R${plano + (p - minutos)*2}')