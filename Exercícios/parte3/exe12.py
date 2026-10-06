'''Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostra a média entre todos
os valores e qual foi o maior e o menor valores lidos.
o programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''
#ler vários números
numero = int(input('Digite um número: '))
continuar = input(' Deseja continuar? sim/não').lower()
n = 1
maximo = numero
minimo = numero
soma = numero
while continuar == 'sim':
    numero= int(input('Digite mais número: '))
    continuar = input(' Deseja continuar? sim/não').lower()
    n += 1
    soma = soma + numero
    if maximo < numero:
        maximo = numero
    if numero < minimo:
        minimo = numero
media = (soma)/n
print(f'A média entre todos os valores é {media} o maior número foi {maximo} e menor {minimo}')
