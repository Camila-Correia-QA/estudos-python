'''Faça um programa que leia nome e média
de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo
de estrutra na tela'''
boletim = dict()
lista = list()
continuar = 'S' or 'N'
while continuar == 'S':
    boletim['nome'] = str(input('Digite o nome do aluno: '))
    boletim ['media'] = float(input('Digite a media '))
    if boletim['media'] >= 7:
        boletim['situacao'] = 'Aprovado'
    if boletim['media'] < 7:
        boletim['situacao'] = 'Reprovado'
    lista.append(boletim.copy())
    continuar = input('Deseja continuar?: S/N ').upper()
    if continuar =='N':
        for k in lista:
            print('----- BOLETIM ------')
            print(f' Nome:{k["nome"]} \n Média:{k["media"]} \n e sua situação é:{k["situacao"]} \n')
