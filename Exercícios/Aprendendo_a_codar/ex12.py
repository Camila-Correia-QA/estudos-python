numero = int(input('Digite um número:'))
print('Escoha 1 se quer converter em número binário')
print('Escoha 2 se quer converter em número octagonal')
print('Escoha 3 se quer converter em número hexadecimal')
escolha = int(input('Digite uma opção:'))
if escolha == 1:
    print(bin(numero)[2:])
elif escolha == 2:
    print(oct(numero)[2:])
elif escolha == 3:
    print(f'{hex(numero)[0:2]}{hex(numero).upper()[2:]}')
else:
    print('Não existe essa opção')