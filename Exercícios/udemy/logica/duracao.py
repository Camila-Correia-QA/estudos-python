#1minuto = 60 segundos
#1hora = 60 minutos
#1hora = 3600 segundos
tempo = int(input('Digite uma duração: '))
horas = tempo // 3600
resto = tempo % 3600
minuto = resto //60
segundos = resto % 60
print(f'{horas}:{minuto}:{segundos}')
14