salario = float(input('Digite seu salário'))
if salario <= 1000:
    print(f'O novo salário será de R${salario * 0.2 + salario}')
    print(f'terá um aumento de  R${salario * 0.2}')
    print(' A porcentagem será de 20%')

elif 3000 >= salario > 1000:
    print(f'O novo salário será de R${salario * 0.15 + salario}')
    print(f'terá um aumento de  R${salario * 0.15}')
    print(' A porcentagem será de 15%')

elif 8000 >= salario > 3000:
    print(f'O novo salário será de R${salario * 0.1 + salario}')
    print(f'terá um aumento de  R${salario * 0.1}')
    print(' A porcentagem será de 10%')

else:
    print(f'O novo salário será de R${salario * 0.05 + salario}')
    print(f'terá um aumento de  R${salario * 0.05}')
    print(' A porcentagem será de 5%')


