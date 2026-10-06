from datetime import date
atleta = input('Digite o nome do atleta:')
ano_nascimento = int(input('Digite o ano de nascimento:'))
ano = date.today().year
idade = ano - ano_nascimento

if idade <= 9:
    print(f'Atleta {atleta} ficará na categoria MIRIM')

elif idade > 9 and idade <= 14:
    print(f' Atleta {atleta} ficará na categoria INFANTIL')

elif idade > 14 and idade <=19:
    print(f' Atleta {atleta} ficará na categoria JÚNIOR')

elif idade == 20:
    print(f'Atleta{atleta} ficará na categoria SÊNIOR')

else:
    print(f'Atleta {atleta} ficará na categoria MASTER')