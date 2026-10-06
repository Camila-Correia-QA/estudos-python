# Variáveis de entrada
import math
print('Bem Vindo Felipe!')
escolha_regiao = input('Escolha uma região A,B,C,D ou E:').upper()

Lx = float(input('Digite o valor da dimensão da x sapata: '))
Ly = float(input('Digite o valor da dimensão da y sapata: '))
P = float(input('Digite o valor da carga vertical: '))
Mx = float(input('Digite o momento fletor em torno do eixo X: '))
My = float(input('Digite o momento fletor em torno do eixo Y: '))
TAdm = float(input('Digite a tensão admissível do solo: \n'))

# Equação 2 e 8

Ex = Mx / P
Ey = My / P
Pm = P / Lx * Ly

# Região A - Equação 18 e 19
if escolha_regiao == 'A':
    Ex = Mx / P

    Ey = My / P

    Pm = P / (Lx * Ly)

    Xn = 4 * Lx * ((1/2)-(abs(Ex)/Lx))

    Yn = 4 * Ly * ((1/2)-(abs(Ey)/Ly))

    Pp = Pq = Pr = P_min = 0

    Po = P_max = (3*Pm)/(8 * ((1/2)-(abs(Ex)/Lx)) * ((1/2)-(abs(Ex)/Ly)))

    print('Valores da região A:')
    print('')
    print(f'Xn = {Xn:.2f} ')
    print(f'Yn = {Yn:.2f} ')
    print(f'Pp = {Pp:.2f} ')
    print(f'Pq = {Pq:.2f} ')
    print(f'Pr = {Pr:.2f} ')
    print(f'P_min = {P_min:.2f} ')
    print(f'Po = {Po:.2f} ')
    print(f'P_max = { P_max:.2f}')
    print(f'Ex = {Ex:.2f}')
    print(f'Ey = {Ey:.2f}')
    print(f'Pm = {Pm:.2f}')




# Região B

if escolha_regiao == 'C':

    Ex = Mx / P

    Ey = My / P

    Pm = P / (Lx * Ly)

    Xn = Lx * (1 + 6 * (abs(Ex)/Lx) + 6 * (abs(Ey)/Ly))/(12*(abs(Ex)/Lx))

    Yn = Ly * (1 + 6 * (abs(Ex)/Lx) + 6 * (abs(Ey)/Ly))/(12*(abs(Ey)/Ly))

    Po = P_max = Pm * (1 + 6 * (abs(Ex)/Lx)) + 6 *(abs(Ey)/Ly)

    Pp = Pm * (1 - 6 * (abs(Ex)/Lx)) + 6 *(abs(Ey)/Ly)

    Pq = Pm * (1 + 6 *(abs(Ex)/Lx) - 6 * (abs(Ey)/Ly))

    Pr = P_min = Pm * (1 - 6 * (abs(Ex)/Lx) - 6 * (abs(Ey)/Ly))

    print(' Valores da região C: \n')
    print(f' Xn = {Xn:.2f}')
    print(f' Yn = {Yn:.2f}')
    print(f' Po = {Po:.2f}')
    print(f' Pp = {Pp:.2f}')
    print(f' Pq = {Pq:.2f}')
    print(f' Pr = {Pr:.2f}\n')
    print(f'P_min = {P_min:.2f} ')
    print(f' P_min = {P_min:.2f}')
    print(f'Ex = {Ex:.2f}')
    print(f'Ey = {Ey:.2f}')
    print(f'Pm = {Pm:.2f}')

# Região D - Equação 21 e 21

if escolha_regiao == 'D':

    Ex = Mx / P

    Ey = My / P

    Pm = P / (Lx * Ly)

    Xn = Lx * (1 +(6 * (abs(Ex)/Lx)) + math.sqrt(1 - 12 * Ex**2/Lx**2))/(12*(abs(Ex)/Lx))

    Yn = 1/2 * Ly * (1/2 - (abs(Ey)/Ly))*(2+ math.sqrt(1-12*Ex**2/Lx**2))*(1+2*abs(Ex)/Lx - math.sqrt(1-12*Ex**2/Lx**2))/(abs(Ex)/Lx*(1+4*Ex**2/Lx**2))

    Yp = Yn * (1- Lx/Xn)

    Po = P_max = Pm / 3 * (2 - math.sqrt(1-12*Ex**2/Lx**2))*(1+6*(abs(Ex)/Lx) + math.sqrt(1-12*Ex**2/Lx**2))/(1/2-(abs(Ey)/Ly))

    Pp =P_max*(1-Lx/Xn)

    Pq = Pr = P_min = 0

    print(' Valores da região D: \n')
    print(f' Xn = {Xn:.2f}')
    print(f' Yn = {Yn:.2f}')
    print(f' Yp = {Yp:.2f}')
    print(f' Po = {Po:.2f}')
    print(f' Pp = {Pp:.2f}\n')
    print(f'P_min = {P_min:.2f} ')
    print(f' P_min = {P_min:.2f}')
    print(f'Ex = {Ex:.2f}')
    print(f'Ey = {Ey:.2f}')
    print(f'Pm = {Pm:.2f}')

if escolha_regiao == 'E':

    Ex = Mx / P

    Ey = My / P

    Pm = P / (Lx * Ly)

    Xn = 1/2 * Lx * (1/2 - (abs(Ex)/Ly))*(2+math.sqrt(1-12*Ey**2/Ly**2))*(1+2*(abs(Ey)/Ly) - math.sqrt(1-12*Ey**2/Ly**2))/(abs(Ey)/Ly*(1+4*Ey**2/Ly**2))

    Yn = Ly * (1 + (6 * abs(Ey)/Ly) + math.sqrt(1-12*Ey**2/Ly**2))/(12*abs(Ey)/Ly)

    Xq = Xn * (1 - Ly/Yn)

    Po = P_max = Pm / 3 * (2 - math.sqrt(1-12*Ey**2/Ly**2))*(1+6*(abs(Ey)/Ly) + math.sqrt(1-12*Ey**2/Ly**2))/(1/2-(abs(Ex)/Lx))

    Pq = P_max * ( 1 - Ly /Yn)

    Pp = Pr = P_min = 0

    print(' Valores da região E: \n')
    print(f' Xn = {Xn:.2f}')
    print(f' Yn = {Yn:.2f}')
    print(f' Xq = {Xq:.2f}')
    print(f' Po = {Po:.2f}')
    print(f' Pq = {Pq:.2f}')
    print(f' Pp = {Pp:.2f}')
    print(f'Ex = {Ex:.2f}')
    print(f'Ey = {Ey:.2f}')
    print(f'Pm = {Pm:.2f}')

if escolha_regiao == 'B':

    Ex = Mx / P

    Ey = My / P

    Pm = P / (Lx * Ly)

    Xn1 = Lx

    Yn1 = Ly

    tolerancia = 0.01

    iteracoes_max = 1000

    iteracao_inicial = 0

while iteracao_inicial < iteracoes_max:

    Xn = 4 * Lx * (1/2 - abs(Ex)/Lx) * ((1-(1-Lx/Xn1)**3-(1-Ly/Yn1)**3)/(1-(1-Lx/Xn1)**4-(1-Ly/Yn1)**4-4*((1-Lx/Xn1)**3)*Lx/Xn1))

    Yn = 4 * Ly * (1/2 - abs(Ey)/Ly) * ((1-(1-Lx/Xn1)**3-(1-Ly/Yn1)**3)/(1-(1-Lx/Xn1)**4-(1-Ly/Yn1)**4-4*((1-Lx/Xn1)**3)*Ly/Yn1))

    Xn = Xn1

    Yn = Yn1

    iteracao_inicial += 1

    if abs(Xn - Xn1) < tolerancia and abs(Yn - Yn1) < tolerancia:
        Xn = 4 * Lx * (1 / 2 - abs(Ex) / Lx) * ((1 - (1 - Lx / Xn1) ** 3 - (1 - Ly / Yn1) ** 3) / (1 - (1 - Lx / Xn1) ** 4 - (1 - Ly / Yn1) ** 4 - 4 * ((1 - Lx / Xn1) ** 3) * Lx / Xn1))

        Yn = 4 * Ly * (1 / 2 - abs(Ey) / Ly) * ((1 - (1 - Lx / Xn1) ** 3 - (1 - Ly / Yn1) ** 3) / (1 - (1 - Lx / Xn1) ** 4 - (1 - Ly / Yn1) ** 4 - 4 * ((1 - Lx / Xn1) ** 3) * Ly / Yn1))

        Xq = Xn * (1-Ly/Yn)

        Yp = Yn * (1-Lx/Xn)

        P_max = 6*(Pm * Lx/Xn * Ly/Yn)/ (1-(1-Lx/Xn)**3-(1-Ly/Yn)**3)

        Po = P_max

        Pp = P_max * (1-Lx/Xn)

        Pq = P_max * (1-Ly/Yn)

        Pr = P_min = 0


print(' Valores da região B: \n')
print(f' Xn = {Xn:.2f}')
print(f' qYn = {Yn:.2f}')
print(f' X = {Xq:.2f}')
print(f' Po = {Po:.2f}')
print(f' Pq = {Pq:.2f}')
print(f' Pp = {Pp:.2f}')
print(f'Ex = {Ex:.2f}')
print(f'Ey = {Ey:.2f}')
print(f'Pm = {Pm:.2f}')
print(f'P_max = {P_max:.2f}')