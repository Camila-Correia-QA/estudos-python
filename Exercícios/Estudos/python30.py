frase=str(input('Digite uma frase:')).lower().strip()
print(f'A letra A aparece {frase.count("a")} vezes')
print(f'ela aparece pela primeira vez na {frase.find("a")} posição')
print(f'A letra A aparece pela ultima vez em {frase.rfind("a")}')