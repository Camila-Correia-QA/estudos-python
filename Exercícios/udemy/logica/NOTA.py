nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
nota_final = nota_1 + nota_2
if nota_final < 60:
    print(f'O aluno ficou com nota {nota_final:.1f} está REPROVADO!!')
else:
    print(f'O aluno ficou com nota {nota_final:.1f} está APROVADO!')