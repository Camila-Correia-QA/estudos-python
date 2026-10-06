alunos = []

continuar = 'S' or 'N'
while continuar == 'S':
    aluno = []
    notas = []
    aluno.append(input('Digite seu nome: '))
    notas.append(int(input('Digite a nota 1: ')))
    notas.append(int(input('Digite a nota 2: ')))
    resultado = (notas[0] + notas[1]) / 2
    aluno.append(resultado)
    aluno.append(notas)
    print(aluno)
    print(notas)
    alunos.append(aluno[:])
    continuar = input('Deseja continuar?: S/N ').upper()
i = 0
for c in alunos:
    print(f'{i} Nome: {c[0]} ----- Média {c[1]}')
    i += 1
restart = int(input('Deseja saber a média de qual aluno?'))
print(f'''As notas do aluno são:
 nota 1: {alunos[restart][2][0]} 
 nota 2: {alunos[restart][2][1]}''')

