'''
Problema "crescente"
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma
mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente. O
programa deve finalizar quando forem digitados dois valores iguais.
'''
x = float(input('Digite um valor para X: '))
y = float(input('Digite um valor para Y: '))

while x != y:
    if x > y:
        print('ORDEM DECRESCENTE')
    else:
        print('ORDEM CRESCENTE')
    x = float(input('Digite um valor para X: '))
    y = float(input('Digite um valor para Y: '))

print(f'PROGRAMA ENCERRADO-{x},{y}')
