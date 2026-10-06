nome= input('Nome do produto')
valor=float(input('O preço do produto custa:'))
desconto = valor*0.05
print(f'O {nome} custa {valor} e com desconto ficará {valor - desconto} ')