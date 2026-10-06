d1 = float(input('Digite um número: '))
d2 = float(input('Digite um número: '))
d3 = float(input('Digite um número: '))
maior_distancia = 0

if d1 > maior_distancia:
    maior_distancia = d1
if maior_distancia > d2 and maior_distancia > d3:
    maior_distancia = d1
if d2 > maior_distancia and d2 > d3:
    maior_distancia = d2
if d3 > d2 and d3> maior_distancia:
    maior_distancia = d3

print(f'A maior distância é {maior_distancia:.2f}')