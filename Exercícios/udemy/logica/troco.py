preco_produto = float(input('Digite o preço do produto: '))
quantidade_produto = int(input('Digite a quantidade: '))
dinheiro_recebido = float(input('Digite o dinheiro recebido: '))
troco = dinheiro_recebido - (preco_produto * quantidade_produto)
if troco >= 0:
    print(f'O troco será de R${troco:.2f}')
else:
    print(f'Faltam R${-troco:.2f} para completar a compra!')
