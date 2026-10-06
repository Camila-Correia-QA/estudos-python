funcionario=input('Digite o nome de um funcionário:')
salario=float(input('Digite o valor do sálário:'))
aumento= 0.15*salario
print(f'O {funcionario} tem um salário de {salario} e ficará com o próximo pagamento de {aumento + salario}')

n = input('QUAL É SEU NOME?')
print(f'Prazer em te conhecer, {n}!') # sem espaços
print(f'Prazer em te conhecer, {n:>100}!') # com 20 espaços