import matplotlib.pyplot as plt

#Define x values as a list

lx= float(input('Digite o valor de Lx: '))
ly= float(input('Digite o valor de Ly: ')) #  largura da sapata
ex = float(input('Digite o valor de Ex: '))
ey = float(input('Digite o valor de Ey: ')) # cordenada do ponto

#Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='y = 2x + 3 (Linear)', color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label='y = x^2 - 4x + 5 (Quadratic)', color='red', marker='o')

#Add labels, title, and legend
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Linear and Quadratic Equations')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Horizontal axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Vertical axis
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.legend()

#Display the plot
plt.show()

