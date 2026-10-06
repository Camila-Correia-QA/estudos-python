r1 = float(input('Digite um valor'))
r2 = float(input('Digite um valor'))
r3 = float(input('Digite um valor'))
if r3 < r1 +r2 and r1 < r2 + r3 and r2 < r1 + r3:
    print('É um triângulo')
else:
    print('Não é um triângulo')