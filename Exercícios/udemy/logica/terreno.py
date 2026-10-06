largura = float(input('Digite a largura: '))
comprimento = float(input('Digite a comprimento: '))
valor = float(input('Digite o valor do metro quadrado: '))
area = largura * comprimento
preco_terreno = area * valor
print(f' A área do terreno equivale a {area:.2f}m² e custa R${preco_terreno:.2f}')