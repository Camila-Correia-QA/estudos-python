'''Crie um programa que tenha uma tupla com várias
palavras(não usar acentos).Depois disso,você deve mostrar, parar
cada palavra, quais são suas vogais.'''
sabores = ('melancia', 'abacaxi', 'banana',
           'abacate', 'baunilha', 'misto',
           'chocolate', 'cacau', 'jaca')
for sabor in sabores:
    vogais = []
    for vogal in sabor:
        if vogal == 'a' or vogal == 'e' or vogal == 'i' or vogal == 'o' or vogal == 'u':
            vogais.append(vogal)
    print(f' na palavra {sabor.title()} temos as vogais {vogais}')

