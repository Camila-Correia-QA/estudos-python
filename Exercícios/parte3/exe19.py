'''Crie um programa que simule o funcionamento de um
caixa eletrônico. No início pergunta ao usuário
qual será o valor a ser sacado e o programa vai informar
quantas cédulas de cada valor serão entregues.
obs:Considere que o caixa possui cédulas de R$50,00, R$ 20,00. R$10,00
R$ 1,00'''
print('-----BANCO DA MILOUCA-----')
dinheiro = int(input('Quanto você quer sacar?'))
cedula_50 = dinheiro // 50
cedula_20 = (dinheiro - (cedula_50 * 50))//20
cedula_10 = (dinheiro - (cedula_50 * 50) - (cedula_20 * 20))//10
cedula_1 = (dinheiro - (cedula_50 *50) - (cedula_20* 20) - (cedula_10 *10))

print(f'Você terá um saque de R${dinheiro} com:')
print(f'{cedula_50} notas de R$50,00')
print(f'{cedula_20} notas de R$20,00')
print(f'{cedula_10} notas de R$10,00')
print(f'{cedula_1}  notas de R$1,00 ')
