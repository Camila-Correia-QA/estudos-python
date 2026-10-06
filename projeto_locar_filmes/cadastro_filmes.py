import os
import os.path
#mensagem de boas vindas
print('Registro de filmes!')
print('Registro de filme escolha a opção:')
print('1 para registrar filme')
print('2 para exibir filme')
print('3 para atualizar filme')
print('4 para excluir filme')
opcao = int(input('Digite a opção desejada:'))
#criar o registro dos filmes
if opcao == 1:
    filme= input('Adicione um filme:')
    arquivo = open(f'filmes/{filme}.txt', 'w')
    arquivo.write(f'{filme}')
    arquivo.close()
    print('Seu filme foi registrado com sucesso!')
#exibir o filme
if opcao == 2:
    print('Você escolheu exibir filme.')
    filme = input('filme para exibir:')
    if (f'filmes/{filme}.txt'):
        arquivo = open(f'filmes/{filme}.txt')
        print(arquivo.read())
    else:
        print('O filme não existe na base de dados!')
#atualizar filme
if opcao == 3:
    print('Você escolheu atualizar o filme.')
    filme = input('filme para pesquisar:')
    if (f'filmes/{filme}.txt'):
        filme = input('Digite o nome do filme:')
        arquivo = open(f'filmes/{filme}.txt', 'w')
        arquivo.write(f'{filme}')
        arquivo.close()
        print('O filme foi atualizado com sucesso!')
    else:
        print('O filme não existe!')
#excluir filme
if opcao == 4:
    print('Você escolheu excluir o filme.')
    filme = input('digite o nome do filme para excluir:')
    if os.path.exists(f'filmes/{filme}.txt'):
        os.remove(f'filmes/{filme}.txt')
        print('Filme removido com sucesso!')
    else:
        print('O filme não existe na base de dados!')