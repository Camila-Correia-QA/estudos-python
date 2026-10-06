''' Crie um programa que tenha uma tupla única com nomes de seus
produtos e seus respectivos preços, na sequência.
No final , mostre uma listagem de preços, organizando
os dados em forma tabular.'''
fachada = '------------ LISTA DE PREÇOS ------------'
produtos = [
            ("Pão", 2.75),
            ("bolo", 18.50),
            ("empada", 8.75),
            ("coxinha", 6.30),
            ("esfirra", 7.50),
]
print('-------------- CARDÁPIO --------------')
print('PRODUTO ................ PREÇO')
for produto in produtos:
    nome, preco = produto
    print(f'{nome:.<6}....................{preco}')


