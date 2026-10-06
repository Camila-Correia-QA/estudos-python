'''Problema "media_idades"
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
mostrar a mensagem "IMPOSSIVEL CALCULAR".'''

x = []
s = 0
idade = int(input('Digite um número: '))
if idade < 0:
    print('IMPOSSÍVEL CALCULAR!')
else:
    while idade > 0:
        x.append(idade)
        s += 1
        idade = int(input('Digite um número: '))
    print(f'A média das idades é {sum(x)/ s}')

