'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.'''
import random
wins = 0
while True:
    par_ou_impar = input('Digite par ou ímpar:').lower()
    escolha = int(input('Escolha um número:'))
    computador = random.randint(0, 11)
    soma = escolha + computador
    if soma %2 == 0:
        print(f'O número é par você jogou {escolha} e o computador jogou {computador}')
        resultado = 'par'
    if soma %2 !=0:
        print(f'O número é ímpar você jogou {escolha} e o computador jogou {computador}')
        resultado = 'ímpar'
    if par_ou_impar == resultado:
        wins += 1
    if par_ou_impar != resultado:
        break
print(f' Você ganhou {wins} vezes no par ou ímpar')







