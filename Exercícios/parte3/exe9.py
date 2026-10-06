# Solicita ao usuário o primeiro termo da progressão aritmética
termo = int(input('Digite o primeiro termo da progressão aritmética: '))

# Solicita ao usuário a razão da progressão aritmética
razao = int(input('Digite a razão da progressão aritmética: '))

# Inicializando contadores
indice = 0  # Contador para o loop principal
atual = 0  # Contador para o número do termo

# Variável que armazena o valor do termo atual
valor = termo

# Número inicial de termos a serem exibidos
limite = 10

# Loop principal que exibe a progressão aritmética
while indice < limite:
    # Calculando o termo atual da progressão aritmética
    valor = termo + atual * razao

    # Incrementando o número do termo e o índice do loop
    atual += 1
    indice += 1

    # Exibindo o termo atual
    print(f'Termo {atual}: {valor}')

    # Verificando se o limite foi atingido
    if indice == limite:
        # Pergunta se o usuário deseja continuar mostrando mais termos
        continuar = input('Você gostaria de continuar exibindo mais termos? (Sim/Não): ')

        # Se o usuário desejar continuar, ajusta o número de termos adicionais
        if continuar.lower() == "sim":
            limite = int(input('Quantos termos adicionais você gostaria de exibir? '))
            indice = 0  # Reinicia o índice para continuar a exibição dos termos