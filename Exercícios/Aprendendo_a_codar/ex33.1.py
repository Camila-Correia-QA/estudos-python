#Desenvolva um programa que leia o nome,idade e sexo de 4
#pessoas.No final do programa mostra:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
#média = idade + idade + idade + idade /4
media_de_idades = 0
idade_homem_mais_velho = 0
nome_homem = 0
qntd_mulher = 0
for c in range(4):
    print(f"{'*'*10} {c +1}ª PESSOA {'*'*10}\n")
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Seu sexo é [M/F]: ').lower()
    media_de_idades = media_de_idades + idade
    if sexo == 'm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem = nome
    if sexo == 'f' and idade < 20:
        qntd_mulher = qntd_mulher +1
    print()

print(f' A média das idades é de {media_de_idades/4}')
if idade_homem_mais_velho == 0:
    print('Não houve homens cadastrados')
else:
    print(f' O nome do homem mais velho é {nome_homem} com idade {idade_homem_mais_velho}')
print(f' A quantidade de mulheres que tem menos de 20 anos são {qntd_mulher}')



