import  math
valor= float(input('Digite um ângulo:'))
angulo=math.radians(valor)
print(f'O ângulo{valor}º tem valor de seno de {math.sin(angulo):.2f}º, cosseno {math.cos(angulo):.2f}º, e a tangente{math.tan(angulo):.2f}º')