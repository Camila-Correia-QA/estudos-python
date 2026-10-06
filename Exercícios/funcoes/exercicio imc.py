'''Calcular a média de peso de todas as pesoas que registraram.
média da altura das pessoas que se registraram.
e calcular o imc dessas medias '''



def imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

lista_peso = []
lista_altura = []
continuar = 'S'
while True:
    if continuar == 'S':
        peso = float(input('Digite seu peso:'))
        lista_peso.append(peso)
        altura = float(input('Digite sua altura:'))
        lista_altura.append(altura)
        i = imc(peso,altura)
        continuar = input('Quer continuar?S/N: ').upper().strip()
    else:
        total = len(lista_altura)
        soma_peso = sum(lista_peso)
        soma_altura = sum(lista_altura)
        print(f'A média  de peso é {soma_peso/total}')
        print(f'A média de altura é {soma_altura/total}')
        print(imc(soma_peso,soma_altura))
        break



print('FIM')
