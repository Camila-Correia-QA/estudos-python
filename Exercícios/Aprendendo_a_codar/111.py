def obter_nome_jogador():
    while True:
        nome = input("Digite o nome do jogador: ")
        if nome.strip():  # Verifica se o nome não é vazio
            return nome
        print("O nome não pode ser vazio. Tente novamente.")

def obter_numero_jogos():
    while True:
        try:
            jogos = int(input("Quantos jogos ele jogou? "))
            if jogos >= 0:
                return jogos
            else:
                print("O número de jogos não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def obter_gols_por_jogo(num_jogos):
    gols_por_jogo = []
    for jogo in range(1, num_jogos + 1):
        while True:
            try:
                gols = int(input(f"Quantos gols ele fez no jogo {jogo}? "))
                if gols >= 0:
                    gols_por_jogo.append(gols)
                    break
                else:
                    print("O número de gols não pode ser negativo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro válido.")
    return gols_por_jogo

def exibir_dados_jogador(nome, gols_por_jogo):
    print(f"\nDados do jogador {nome}:")
    for i, gols in enumerate(gols_por_jogo, 1):
        print(f"Jogo {i}: {gols} gol(s)")

def main():
    nome = obter_nome_jogador()
    num_jogos = obter_numero_jogos()
    if num_jogos > 0:
        gols_por_jogo = obter_gols_por_jogo(num_jogos)
        exibir_dados_jogador(nome, gols_por_jogo)
    else:
        print(f"O jogador {nome} não jogou nenhuma partida.")

# Chamada principal do programa
main()