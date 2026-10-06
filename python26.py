num = int(input('Informe um número: '))
u = num // 1 % 10
d= num // 10% 10
ce= num // 100% 10
m= num // 1000% 10

print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'dezena {d}')
print(f'f centena {ce}')
print(f' milhar {m}')