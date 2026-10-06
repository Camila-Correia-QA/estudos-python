nome = input('Digite seu nome:')
peso = float(input('Digite seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura**2)
if imc < 18.5:
    print(f' {nome} está com imc de {imc:.2f} e está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'{nome} está com imc de {imc:.2f} e está no peso ideal!')
elif imc >= 25 and imc < 30:
    print(f'{nome} está com imc de {imc:.2f} e está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print(f'{nome} está com imc de {imc:.2f} e está com obesidade!')
else:
    print(f'{nome} está com imc de {imc:.2f} e está com obesidade mórbida!')

