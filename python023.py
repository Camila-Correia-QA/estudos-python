numero=int(input('Digite um número:'))
u= numero// 1 % 10
d= numero// 10 % 10
c= numero// 100 % 10
m = numero// 1000 % 10
print(f'Analisando o número {numero}')
print(f'Possui unidade {u}')
print(f'Possui dezena {d}')
print(f'Possui centena {c}')
print(f'Possui milhar {m}')