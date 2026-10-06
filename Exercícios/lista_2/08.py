'''Crie um programa que leia nome e duas notas
de vários alunos e guarde tudo em lista composta.
No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente.'''

alunos = []
aluno = []
notas = []
continuar = 'S' or 'N'
while continuar == 'S':
    aluno.append(input('Digite seu nome: '))
    notas.append(int(input('Digite a nota 1: ')))
    notas.append(int(input('Digite a nota 2: ')))
    resultado = (notas[0] + notas[1]) / 2
    aluno.append(resultado)
    print(aluno)
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = input('Deseja continuar?: S/N ').upper()
i = 0
for c in alunos:
    print(f'{i} Nome: {c[0]} ----- Média {c[1]}')
    i += 1
restart = int(input('Deseja saber a média de qual aluno?'))
print(f'{alunos[restart]}')

