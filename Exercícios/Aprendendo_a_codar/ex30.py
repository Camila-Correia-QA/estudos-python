#Crie um programa que leia ma frase qualquer e diga se ela
#é um palíndromo, desconsiderando os espaços.
nome = input('Digite uma frase:').replace(' ','').lower()
print(f'{nome.strip()}')
if nome == nome[::-1]:
    print('É um  palíndromo')
else:
    print('Não é um palíndromo')
