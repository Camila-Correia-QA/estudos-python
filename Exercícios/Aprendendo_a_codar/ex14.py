from datetime import date
nome = input('Qual o seu nome?:')
nascimento = int(input('Qual seu ano de nascimento?:'))
ano = date.today().year
idade = ano - nascimento
print(f'{idade}')
if idade == 17:
    print('Você deve se alistar ao serviço militar!')
elif idade > 17 and idade < 25:
    print('Já está na hora de se alistar para o serviço militar!!')
elif idade > 24:
    print(f' Você não tem mais idade para se alistar para o serviço militar já passou {idade - 18} anos!')
else:
    print(f'Você não tem idade suficiente para se alistar faltam {17 - idade} anos para se alistar!')