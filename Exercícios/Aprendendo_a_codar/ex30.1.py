frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase {junto} inversa fica {inverso} é um palíndromo.')
else:
    print(f'A frase {junto} inversa fica {inverso} não é um palíndromo.')