import itertools
import random

# Definir o intervalo de números e o tamanho das combinações
numeros = range(1, 61)
tamanho_combinacao = 6

# Lista de posições fornecidas
posicoes = range(1, 50063860)

# Escolher uma posição aleatória da lista
indice_desejado = random.choice(posicoes) - 1  # Subtrai 1 para o índice Python

# Gerar a combinação de índice específico
combinacao_especifica = next(itertools.islice(itertools.combinations(numeros, tamanho_combinacao), indice_desejado, None))

# Exibir o resultado
print(f"Combinação na posição {indice_desejado + 1}:", combinacao_especifica)

