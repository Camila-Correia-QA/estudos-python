temperature = ''
while temperature != 'C' and temperature != 'F':
    temperature = input('Você vai digitar a temperatura em qual escala? C/F').upper()

if temperature == 'C':
    c = float(input('Digite a temperatura em Celsius:'))
    graus_f = c * 1.8 + 32
    print(f'A temperatura em Fahrenheit será {graus_f}')

else:
    f = float(input('Digite a temperatura em Fahrenheit:'))
    graus_c = 5 / 9*(f - 32)
    print(f'A temperatura em Celsius será {graus_c}')



