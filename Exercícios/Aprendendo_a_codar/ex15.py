nome = input('Digite o nome do aluno:')
materia = input('Digite a matéria:')
nota1 = float(input('Digite a nota do teste:'))
nota2 = float(input('Digite a nota da prova:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f' {nome} ficou com média {media} em {materia} está REPROVADO!')
elif media >=  5.0 and media <= 6.9:
    print(f' {nome} ficou com média {media} em {materia} vai para a RECUPERAÇÃO!')
else:
    print(f' {nome} ficou com média {media:.2f} em {materia} e está APROVADO!!! PARABÉNS')
