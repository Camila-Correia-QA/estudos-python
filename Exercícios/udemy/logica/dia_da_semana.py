
diasDaSemana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta','sexta','sábado']
semana = int(input('Digite um número: '))
if semana >=1 and semana <= 7:
    print(f' o dia da semana é {diasDaSemana[semana-1]}')
else:
    print('Esse dia da semana não existe')