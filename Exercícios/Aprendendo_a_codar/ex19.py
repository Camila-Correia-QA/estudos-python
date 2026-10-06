produto = input('Digite o nome do produto:')
valor_produto = float(input('Digite o valor do produto:'))
print('Escolha a opção de pagamento:')
print('1 para pagamento à vista dinheiro/cheque')
print('2 para pagamento à vista no cartão')
print('3 para pagamento em até 2x no cartão')
print('4 para pagamento em 3x ou mais no cartão')
forma_de_pagamento = int(input('Digite um número pra a opção de pagamento:'))

if forma_de_pagamento == 1:
    print(f'O valor de {produto} ficará R${valor_produto -(valor_produto * 0.1):.2f}')

elif forma_de_pagamento == 2:
    print(f'O valor de {produto} ficará R${valor_produto -(valor_produto * 0.05):.2f}')

elif forma_de_pagamento == 3:
    print(f'O valor de {produto} ficará duas parcelas de R$ {valor_produto/2:.2f}')

elif forma_de_pagamento == 4:
    parcela = int(input('Quantas vezes você deseja parcelar?'))
    print(f' O valor de {produto} ficará {parcela} parcelas de R$ {valor_produto/parcela + (valor_produto*0.2)/parcela}')