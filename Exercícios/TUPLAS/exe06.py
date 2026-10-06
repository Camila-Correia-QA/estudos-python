''' Crie um programa que tenha uma tupla única com nomes de seus
produtos e seus respectivos preços, na sequência.
No final , mostre uma listagem de preços, organizando
os dados em forma tabular.'''
listagem = ('Pão', 2.75, 'bolo', 18.50, 'empada', 8.75, 'coxinha', 6.30, 'esfirra', 7.50)
precos_l = '---------- LISTA DE PREÇOS ----------'
precos = []
itens = []
print(precos_l)
print(f'----------{listagem[0:2:]}-----------')
print(f'----------{listagem[2:4:]}----------')
print(f'----------{listagem[4:6]}--------')
print(f'----------{listagem[8:]}--------')

