nome = 'Camila Correia'
altura= 1.63
peso =  57
imc = peso / altura**2

print (nome ,'tem', altura ,'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)


linha_1= f' {nome} tem {altura:.2f} de altura'
linha_2 =f'{peso} quilos e seu IMC é '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))