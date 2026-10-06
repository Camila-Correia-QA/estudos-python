hora_inicial = int(input('Digite a hora inicial: '))
hora_final = int(input('Digite a hora final: '))
duracao = 24 - hora_inicial + hora_final
mesmoDia = hora_final - hora_inicial
if hora_inicial > hora_final:
    print(f' O game teve duração de {duracao}')
else:
    print(f' O game teve a duração de {mesmoDia}')