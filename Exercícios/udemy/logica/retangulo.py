import math
base = float(input('Digite a base: '))
altura = float(input('Digite a base: '))
area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = math.sqrt((base ** 2) + (altura ** 2))

print(f' A área equivale a {area} \n'
      f' Perimentro {perimetro} \n'
      f' Diagonal {diagonal}')