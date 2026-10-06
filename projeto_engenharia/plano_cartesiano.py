import matplotlib.backend_bases
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import random

# Função para gerar uma cor aleatória, mas visível
import matplotlib.backend_bases
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
import random


# Função para gerar uma cor aleatória, mas visível
def gerar_cor_visivel():
    # Gerar cores no espectro RGB, mas evitando cores claras ou muito escuras
    while True:
        cor = [random.random(), random.random(), random.random()]
        # Verificar se a cor é suficientemente contrastante
        luminosidade = 0.2126 * cor[0] + 0.7152 * cor[1] + 0.0722 * cor[2]  # Luminosidade
        if luminosidade > 0.3 and luminosidade < 0.7:  # Evita cores muito claras ou muito escuras
            return cor


def plano_cartesiano():
    # Configurações iniciais
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10

    # Estruturas de dados
    pontos: set[tuple[float, float]] = set()  # Armazena pontos únicos
    marcacoes = []
    linhas = []

    # Criar figura e eixos
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.subplots_adjust(left=0.1, bottom=0.3)

    # Configuração inicial do gráfico
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    plt.title("Plano Cartesiano")

    # Criar caixas de entrada para limites
    ax_input_x_min = plt.axes([0.27, 0.15, 0.15, 0.05])
    ax_input_x_max = plt.axes([0.50, 0.15, 0.15, 0.05])
    ax_input_y_min = plt.axes([0.27, 0.05, 0.15, 0.05])
    ax_input_y_max = plt.axes([0.50, 0.05, 0.15, 0.05])

    input_x_min = TextBox(ax_input_x_min, "X Min", initial=str(x_min))
    input_x_max = TextBox(ax_input_x_max, "X Max", initial=str(x_max))
    input_y_min = TextBox(ax_input_y_min, "Y Min", initial=str(y_min))
    input_y_max = TextBox(ax_input_y_max, "Y Max", initial=str(y_max))

    # Função auxiliar para limpar tela
    def limpar_tela():
        for marcacao in marcacoes:
            marcacao.remove()
        for linha in linhas:
            linha.remove()
        marcacoes.clear()
        pontos.clear()
        linhas.clear()
        fig.canvas.draw_idle()

    # Função para atualizar os limites
    def atualizar_limites():
        try:
            x_min_val = float(input_x_min.text)
            x_max_val = float(input_x_max.text)
            y_min_val = float(input_y_min.text)
            y_max_val = float(input_y_max.text)

            ax.set_xlim(x_min_val, x_max_val)
            ax.set_ylim(y_min_val, y_max_val)
            fig.canvas.draw_idle()
        except ValueError:
            print("Insira valores numéricos válidos.")

    # Botão para resetar o gráfico
    ax_botao_reset = plt.axes([0.67, 0.1, 0.1, 0.07])
    botao_reset = Button(ax_botao_reset, "Reset")
    botao_reset.on_clicked(lambda event: limpar_tela())

    # Função para verificar se já existe um ponto na posição clicada
    def ponto_existente(x: float, y: float) -> bool:
        return (round(x, 2), round(y, 2)) in pontos

    # Função para adicionar pontos
    def adicionar_ponto(event: matplotlib.backend_bases.MouseEvent):
        if event.inaxes == ax:
            x, y = round(event.xdata, 2), round(event.ydata, 2)

            if ponto_existente(x, y):
                print(f"Ponto ({x}, {y}) já existe.")
                return

            pontos.add((x, y))

            # Gerar cores aleatórias para ponto e linha
            cor_ponto = gerar_cor_visivel()
            cor_linha = cor_ponto

            ponto_plotado, = ax.plot(x, y, 'o', color=cor_ponto)
            texto = ax.text(x + 0.2, y + 0.2, f"({x}, {y})", fontsize=8, color=cor_ponto)
            marcacoes.extend([ponto_plotado, texto])

            linha_horizontal, = ax.plot([0, x], [y, y], '--', color=cor_linha, linewidth=0.8)
            linha_vertical, = ax.plot([x, x], [0, y], '--', color=cor_linha, linewidth=0.8)
            linhas.extend([linha_horizontal, linha_vertical])

            fig.canvas.draw_idle()

    # Conectar eventos
    fig.canvas.mpl_connect("button_press_event", adicionar_ponto)

    # Conectar evento para atualização dos limites ao mudar os valores dos inputs
    input_x_min.on_submit(lambda text: atualizar_limites())
    input_x_max.on_submit(lambda text: atualizar_limites())
    input_y_min.on_submit(lambda text: atualizar_limites())
    input_y_max.on_submit(lambda text: atualizar_limites())

    plt.show()


# Executar
plano_cartesiano()
plano_cartesiano.py
5
KB