glicose = float(input('Digite sua glicose: '))
if glicose <= 100:
    print('Seu nível de glicose está normal')
elif 100 < glicose <= 140:
    print('Seu nível de glicose está elevado')
elif glicose > 140:
    print('Você está com diabetes')