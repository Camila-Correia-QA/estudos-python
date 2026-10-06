#CREATE
#READ
#UPDATE
#DELETE

import mysql.connector

conexao = mysql.connector(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'bdyyoutube',

)

cursor = conexao.cursor()

#CRUD
#CREAT
nome_produto = "toddynho"
valor = 3
comando = f'INSERT TO vendas (nome_produto, valor)VALUES ({nome_produto},{valor})'
cursor.execute(comando)
conexao.commit()#edita o banco de dados
#resultado = cursor.fetchall() # ler bancos de dados

#CREAT

nome_produto = "toddynho"
valor = 3
comando = f'INSERT TO vendas (nome_produto, valor)VALUES ({nome_produto},{valor})'
cursor.execute(comando)
conexao.commit()

#READ

comando = f'select  * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

#UPDATE

nome_produto = "toddynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE

nome_produto = "toddynho"
valor = 3
comando = (f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
