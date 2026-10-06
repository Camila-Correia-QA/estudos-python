import random

# Definir o intervalo de números e o tamanho das combinações
numeros = range(1, 61)
tamanho_combinacao = 6

# Calcular o índice da combinação desejada
indice_desejado = 44037888 - 1  # Subtrai 1 porque o índice em Python começa do zero

# Gerar a combinação de índice específico
combinacao_especifica = next(itertools.islice(itertools.combinations(numeros, tamanho_combinacao), indice_desejado, None))

# Exibir o resultado
print(f'-> {combinacao_especifica}')


print('')
