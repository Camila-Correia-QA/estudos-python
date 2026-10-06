r1 = float(input('Digite um valor'))
r2 = float(input('Digite um valor'))
r3 = float(input('Digite um valor'))

if r3 < r1 +r2 and r1 < r2 + r3 and r2 < r1 + r3:
    print('É um triângulo')

    if r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo escaleno!')

    elif (r1 == r2 ) or (r1 == r3) or(r2 == r3):
        print('É um triângulo isósceles!')

    elif (r1 == r2) and (r1 == r3):
        print('É um triângulo equilátero!')

else:
    print('Não é um triângulo')
