'''Faça um programa que receba 3 notas.

E que use as duas maiores para fazer uma media.

Se a media for maior que 7 o Aluno é aprovado por nota.
Se a media for menos que 3 o aluno é reprovado por nota.
Se a media for maior que 3 e menor que 7 o Aluno ficará para Avaliação final.'''

notas = []

nota_1 = float(input('Digite a primeira nota: '))

nota_2 = float(input('Digite a primeira nota: '))

nota_3 = float(input('Digite a primeira nota: '))

notas.append(nota_1)
notas.append(nota_2)
notas.append(nota_3)


if nota_1 < 0 or nota_2 < 0 or nota_3 < 0:
    print('Essa nota não pode ser gerada!')
    quit()

media = (nota_1 + nota_2 +nota_3 - min(notas)) / 2

print(f'{min(notas)}')

if media >= 7:
    print(f'O aluno está aprovado!! com nota {media:.2f}')

elif media < 3:
    print(f'O aluno está reprovado com a média {media:.2f} ')

else:
    print(f'O aluno está reprovado com nota {media:.2f},  mas terá direito a recuperação!')


