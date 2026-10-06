'''uma função que recebe um texto de parametro,
a função deve contar quantas vogais tem nesse
texto e retornar o valor.'''

def texto():
    s = 0
    t = input('Digite uma frase: ').lower()
    for a in t:
        if a == 'a'or 'e' or 'i' or 'o' or 'u':
            s += 1
        print(s)

texto()
