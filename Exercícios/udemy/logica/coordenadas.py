'''
Q1 = X->+ / Y ->+
Q2 =  X -> - / Y -> +
Q3 =  X - > - / Y -> -
Q4 = X - > + / Y= ->-
ORIGEM = X = 0 AND Y = 0
EIXO X => Y = 0
EIXO Y => X = 0'''
x = float(input('Digite um valor x: '))
y = float(input('Digite um valor y: '))

if x == 0 and y == 0:
    print('O ponto se encontra na origem')

if x == 0:
    print('O ponto se encontra no eixo Y')

if y == 0:
    print('O ponto se encontra no eixo X')

if x > 0 and y > 0:
    print('O ponto se encontra no 1º quadrante')

if x < 0 and y > 0:
    print('O ponto se encontra no 2º quadrante')

if x < 0 and y < 0:
    print('O ponto se encontra no 3º quadrante')

if x > 0 and y < 0:
    print('O ponto se encontra no 4º quadrante')

