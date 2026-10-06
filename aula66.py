while True:
    numero_1= input('Digite um número:')
    numero_2= input('Digite outro número')
    operador= input('Digite o operador( +-/*):')

    numeros_validos= None

    try:
        num_1_float= float(numero_1)
        num_2_float=float(numero_2)
        numeros_validos = True
    except:
        numeros_validos= None

        if numeros_validos is None:
            print('Um ou ambos os números digitados são inválidos.')
            continue