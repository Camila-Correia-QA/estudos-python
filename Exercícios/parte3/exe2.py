#Faça um programa que leia o sexo de uma pessoa,
#mas só aceita os valores "M" ou "F". Caso esteja errado,
#peça a digitação novamente até ter um valor correto.
sexo = input('Digite seu sexo:').upper()
while sexo != 'M' and sexo != 'F':
    print('SEXO NÃO IDENTIFICADO! DIGITE NOVAMENTE SEU SEXO:')
    sexo = input('Digite seu sexo:').upper()
print(f'Seu sexo é {sexo}!')



