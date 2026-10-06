import os
import os.path

#mesagem de boas vindas e instrução de como se cadastra
print('Cadastro de cliente escolha a opção:')
print('1 para criar cliente')
print('2 para atualizar cliente')
print('3 para excluir cliente')
print('4 para consultar o cliente')
opcao = int(input('Digite a opção desejada:'))

#criar cliente
if opcao == 1:
    print('Você escolheu criar cliente.')
    nome = input('nome do cliente:')
    cpf = input('cpf do cliente:')
    arquivo = open(f'clientes/{cpf}.txt', 'w')
    arquivo.write(f'{nome}, {cpf}')
    arquivo.close()
    print('Seu cadastro foi realizado com sucesso!')

#atualizar cliente
if opcao == 2:
    print('Você escolheu atualizar cliente.')
    cpf = input('cpf do cliente para pesquisar:')
    if os.path.exists(f'clientes/{cpf}.txt'):
        nome = input('Digite o nome do cliente:')
        arquivo = open(f'clientes/{cpf}.txt', 'w')
        arquivo.write(f'{nome}, {cpf}')
        arquivo.close()
        print('Seu cadastro foi atualizado com sucesso!')
    else:
        print('O CPF não existe!')

#excluir cliente
if opcao == 3:
    print('Você escolheu excluir cliente.')
    cpf = input('cpf do cliente para  excluir:')
    if os.path.exists(f'clientes/{cpf}.txt'):
        os.remove(f'clientes/{cpf}.txt')
        print('Cliente removido com sucesso!')
    else:
        print('O CPF não existe na base de dados!')

if opcao == 4:
    print('Você escolheu consultar cliente.')
    cpf = input('cpf do cliente para consultar:')
    if os.path.exists(f'clientes/{cpf}.txt'):
        arquivo = open(f'clientes/{cpf}.txt')
        print(arquivo.read())
    else:
        print('O CPF não existe na base de dados!')