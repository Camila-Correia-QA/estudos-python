'''Crie um programa que leia a idade e  sexo de várias
pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar.No final mostre:
a)quantas pessoas tem mais de 18 anos.
b)quantos homens foram cadastrados.
c)quantas mulheres em menos de 20 anos.'''
lista_nome = []
lista_idade = []
lista_sexo = []
maior_que = 0
homens_cadastrados = 0
mulheres_menor = 0
continuar = 'S'
while True:
    if continuar == 'S':
        nome = input('Digite seu nome: ')
        lista_nome.append(nome)
        idade = int(input('Digite sua idade: '))
        lista_idade.append(idade)
        if idade > 18:
            maior_que += 1
        sexo = input('Digite seu sexo F / M: ').upper()
        lista_sexo.append(sexo)
        if sexo == 'M':
            homens_cadastrados += 1
        continuar = input('Quer continuar? S / N: ').upper()
        if sexo =='M' and idade > 20:
            mulheres_menor += 1

    if continuar == 'N':
        break
#a)quantas pessoas tem mais de 18 anos.
print(f'Os números na lista maior que 18 são {maior_que}')
#b)quantos homens foram cadastrados.
print(f'Foram cadastrados {homens_cadastrados} homens')
#c)quantas mulheres tem menos de 20 anos.'''
print(f'{mulheres_menor} mulheres tem menos de 20 anos')







