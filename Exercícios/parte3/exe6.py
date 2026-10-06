n = int(input("Digite um número:"))
i = 1
n_fat = 1
while i <= n:
    n_fat = n_fat * i
    i += 1
print(f"O valor de fatorial {n}! é: {n_fat}")