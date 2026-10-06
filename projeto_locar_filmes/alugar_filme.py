import os
import os.path
import shutil
#se o filme ta disponível
print('Verifique se o filme está disponível:')
filme = input('Digite o nome do filme:')
#se sim está disponível: eu alugo para o cliente
if not os.path.exists(f'filmes/{filme}.txt'):
    print('O filme digitado não existe no registro.')

elif not os.path.exists(f'filmes_alugados/{filme}.txt'):
    print('O filme está disponível')
    cpf = input('cpf do cliente:')
    print(f' {cpf} alugará o {filme} ')
    arquivo = open(f'filmes_alugados/{filme}.txt', 'w')
    arquivo.write(str(cpf))
    arquivo.close()
#se não: eu mostro com quem está esse filme
else:
    arquivo = open(f'filmes_alugados/{filme}.txt')
    cpf = arquivo.read()
    cliente = open(f'clientes/{cpf}.txt')
    dados = cliente.read()
    nome = dados.split(',')[0]
    print(f'O filme {filme} não está disponível e se encontra com {nome}')


