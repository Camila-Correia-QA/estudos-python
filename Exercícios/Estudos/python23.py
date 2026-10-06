nome = input('Digite seu nome')
print(f'Seu nome todo maiúsculo fica {nome.upper()}')
print(f'Seu nome todo minúsculo fica {nome.lower()}')
nome_sem_espaço=nome.replace(" ","")
print(len(nome_sem_espaço))
print(f' seu nome tem {len(nome) - nome.count(" ")} letras')
print(f' Seu primeiro nome tem {len(nome.split()[0])} ')

