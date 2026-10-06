def caixa_eletronico(valor):
    cedulas = [50, 20, 10, 1]
    qtd_cedulas = {}

    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            valor = valor % cedula
            qtd_cedulas[cedula] = quantidade

    for cedula in cedulas:
        if cedula in qtd_cedulas:
            print(f"Cédulas de {cedula}: {qtd_cedulas[cedula]}")


valor = int(input("Digite o valor a ser sacado: R$ "))
caixa_eletronico(valor)