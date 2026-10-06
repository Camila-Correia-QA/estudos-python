import matplotlib.pyplot as plt
import numpy as np

# Criar os dados para o gráfico (opcional)
x = np.linspace(-10, 8, 100)  # Cria 100 pontos entre -10 e 10
y = np.linspace(-10, 8, 100)  # Cria 100 pontos entre -10 e 10

lx= float(input('Digite o valor de Lx: '))
ly= float(input('Digite o valor de Ly: '))

vertice_1= (lx/2,ly/2)
vertice_2= (-lx/2,ly/2)
vertice_3= (-lx/2,-ly/2)
vertice_4= (lx/2,-ly/2)
vertice_retangulo = [vertice_1,vertice_2, vertice_3, vertice_4]

poligono = patches.Polygon(vertices, closed=True, edgecolor='blue', facecolor='lightblue', linewidth=2)

# Criar o plano cartesiano
plt.axhline(0, color='black', linewidth=1)  # Linha horizontal no eixo y=0
plt.axvline(0, color='black', linewidth=1)  # Linha vertical no eixo x=0
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adiciona uma grade

# Plotar uma função (opcional)

plt.plot(x, y, label='lx,ly', color='red')  # Função linear

# Configurar o gráfico
plt.title('Plano Cartesiano')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.legend()  # Adiciona a legenda
plt.xlim(-10, 10)  # Define os limites do eixo X
plt.ylim(-10, 10)  # Define os limites do eixo Y

# Exibir o gráfico
plt.show()
