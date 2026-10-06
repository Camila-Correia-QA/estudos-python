#Crie um programa que tenha tupla totalmente preenchida
#com uma contagem por extenso, de zero até 20.
#Seu programa deverá ler um número pelo teclado
#(entre 0 e 20) e mostrá-lo por extenso.
numbers = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove', 'vinte')
continuar = 's'
while True:
    contagem = int(input('Digite um número entre 0 e 20: '))
    if contagem > 20 or contagem < 0:
        print('Por favor digite um número inteiro entre 0 e 20')
    if 0 <= contagem <= 20:
        print(f'Você digitou o número {numbers[contagem]}')
        continuar = input('Deseja continuar?').upper()
        if continuar != 'S':
            break


