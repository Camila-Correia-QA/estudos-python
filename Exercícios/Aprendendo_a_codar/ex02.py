import random
num = (random.randint(1,5))
numero = int(input('Adivinhe o número que estou pensando:'))
if numero == num:
    print('Parabéns você adivinhou o número')
else:
    print('Que pena, tente outra vez!')
print(f' o número era {num}')