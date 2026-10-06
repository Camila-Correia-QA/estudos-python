import random

from time import sleep

jkp = ['pedra', 'papel', 'tesoura']

jogada = input('Jogue PEDRA, PAPEL OU TESOURA: ').lower()
while jogada != 'pedra' or jogada!= 'papel' or jogada != 'tesoura':
    print('tente novamente: ')
    jogada = input('Jogue PEDRA, PAPEL OU TESOURA: ').lower()
    if jogada == 'pedra' or jogada == 'papel' or jogada == 'tesoura':
        break



print('PEDRA')

sleep(1)

print ('PAPEL')

sleep(1)

print('TESOURA')

sleep(1)

print('...')

computador_escolhe = (random.choice(jkp))
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

if computador_escolhe == 'pedra' and jogada == 'tesoura':

    print('Que pena você tomou uma pedrada! MUAHAHAHA')

elif computador_escolhe == 'pedra' and jogada =='papel':

    print('PARABÉNS VOCÊ EMBRULHOU A PEDRA IGUAL UM LIXO WEEEEE')

elif computador_escolhe == 'papel' and jogada == 'pedra':

    print('Que pena você foi embrulhado igual um lixo:')

elif computador_escolhe == 'papel' and jogada == 'tesoura':

    print('PARABÉNS VOCÊ FEZ DE PICADINHO ESSE PAPEL!!! MUHAHAHAHAHA')

elif computador_escolhe == 'tesoura' and jogada == 'papel':

    print('TRAMONTINA CORTE RÁPIDO, VOCÊ FOI PICOTADO COM SUCESSO!! :( ')

elif computador_escolhe == 'tesoura' and jogada == 'pedra':

        print('COLOCA O CAPACETE QUE LÁ VEM PEDRADA WEEEEEEE, ARRASOU , VOCÊ APEDREJOU SEU INIMIGO!!')

else:
    print('Tente novamente, ocorreu empate!!')

print(f'Você jogou {jogada} e seu inimigo {computador_escolhe}!')