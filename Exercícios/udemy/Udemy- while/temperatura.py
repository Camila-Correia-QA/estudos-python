continuar = 'S'
while continuar == 'S':
    c = float(input('Digite uma temperatura: '))
    f = (9 * c )/ 5 + 32
    print(f' Equivalência em Fahrenheit {f}')
    continuar = input('Deseja continuar S/N? ').upper()
print('FIM')






