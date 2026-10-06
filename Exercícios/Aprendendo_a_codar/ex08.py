print(' Olá, seja bem vindo, por favor não utilize vírgulas ou pontos')
valor_do_salario = float(input('Qual o seu salário?'))
if valor_do_salario > 1250:
    print(f'O salário ficará R$ {valor_do_salario * 0.10 + valor_do_salario}')
else:
    print(f'O salário ficará R$ {valor_do_salario * 0.15 + valor_do_salario}')