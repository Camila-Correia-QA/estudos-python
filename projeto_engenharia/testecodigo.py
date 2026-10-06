import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
from shapely.geometry import Point, Polygon as ShapelyPolygon
from math import  sqrt

lx= float(input('Digite o valor de Lx: '))
ly= float(input('Digite o valor de Ly: ')) #  largura da sapata
ex = float(input('Digite o valor de Ex: '))
ey = float(input('Digite o valor de Ey: ')) # cordenada do ponto

#formulas

a1 = (ex**2) / (lx**2)
a2 = abs(ex)/ly
a3 = sqrt(1-12*a1)

steps = 6
x0 = ly/ 4
xf = 0
x_valores = [x0 - (x0/ (steps - 1 ))* i for i in range (steps)]
lista_y = []

for x in x_valores:
    a1 = (ex ** 2) / (lx ** 2)
    a2 = abs(ex) / ly
    a3 = sqrt(1 - 12 * a1)
    y = 0.5 - [1/6 * (2-a3) * (1+2 * a2 + a3)/(1+4*a2)]
    lista_y.append(y)

    

# Define the areas

p1 = (lx/2, ly/2)
p2 = (lx/4, ly/2)
p3 = (lx/4, ly/4)
p4 = (lx/2, ly/4)

p5 = (-lx/4, ly/2)
p6 = (-lx/2, ly/2)
p7 = (-lx/2, ly/4)
p8 = (-lx/4, ly/4)

p9 =  (-lx/4, -ly/4)
p10 = (-lx/2, -ly/4)
p11 = (-lx/2, -ly/2)
p12 = (-lx/4, -ly/2)

p13 = (lx/2, -ly/4)
p14 = (lx/4, -ly/4)
p15 = (lx/4, -ly/2)
p16 = (lx/2, -ly/2)
p17 = (lx/6, 0)
p18 = (0, ly/6)
p19 = (-lx/6,0)
p20 = (0,-ly/6)

area1 = ShapelyPolygon([(p1),(p2),(p3),(p4)])
area2 = ShapelyPolygon([(p5),(p6),(p7),(p8)])
area3 = ShapelyPolygon([(p9),(p10),(p11),(p12)])
area4 = ShapelyPolygon([(p13),(p14),(p15),(p16)])


area5 = ShapelyPolygon([(p3),(p17),(p18)])
area6 = ShapelyPolygon([(p8),(p18),(p19)])
area7 = ShapelyPolygon([(p9),(p19),(p20)])
area8 = ShapelyPolygon([(p17),(p14),(p20)])

area9 = ShapelyPolygon([(p17),(p18),(p19),(p20)])


area10 = ShapelyPolygon([(p4),(p13),(p14),(p17),(p3)])
area11 = ShapelyPolygon([(p7),(p8),(p19),(p9),(p10)])

area12 = ShapelyPolygon([(p2),(p5),(p8),(p18),(p3)])
area13 = ShapelyPolygon([(p9),(p12),(p15),(p14),(p20)])
# Plot the areas
fig, ax = plt.subplots()

#area A

area_a = Polygon([(p1),(p2),(p3),(p4)],closed=True, color='red', alpha=0.3)
ax.add_patch(area_a)

area_a2 = Polygon([(p5),(p6),(p7),(p8)],closed=True, color='red', alpha=0.3)
ax.add_patch(area_a2)

area_a3 = Polygon([(p9),(p10),(p11),(p12)],closed=True, color='red', alpha=0.3)
ax.add_patch(area_a3)

area_a4 = Polygon([(p13),(p14),(p15),(p16)],closed=True, color='red', alpha=0.3)
ax.add_patch(area_a4)

areas_a = [area1, area2, area3, area4]

#area B

area_b = Polygon([(p3),(p17),(p18)],closed=True, color='yellow', alpha=0.3)
ax.add_patch(area_b)

area_b2 = Polygon([(p8),(p18),(p19)],closed=True, color='yellow', alpha=0.3)
ax.add_patch(area_b2)

area_b3 = Polygon([(p9),(p19),(p20)],closed=True, color='yellow', alpha=0.3)
ax.add_patch(area_b3)

area_b4 = Polygon([(p17),(p14),(p20)],closed=True, color='yellow', alpha=0.3)
ax.add_patch(area_b4)

areas_b = [area5, area6, area7, area8]

# area C

area_c = Polygon([(p17),(p18),(p19),(p20)],closed=True, color='blue', alpha=0.3)
ax.add_patch(area_c)


#area D

area_d = Polygon([(p4),(p13),(p14),(p17),(p3)],closed=True, color='orange', alpha=0.3)
ax.add_patch(area_d)

area_d2 = Polygon([(p7),(p8),(p19),(p9),(p10)],closed=True, color='orange', alpha=0.3)
ax.add_patch(area_d2)

areas_d = [area10, area11]

#area E

area_e = Polygon([(p2),(p5),(p8),(p18),(p3)],closed=True, color='purple', alpha=0.3)
ax.add_patch(area_e)

area_e2 = Polygon([(p9),(p12),(p15),(p14),(p20)],closed=True, color='purple', alpha=0.3)
ax.add_patch(area_e2)

areas_e = [area12, area13]

# Define and plot a dot
dot = ( ex, ey )
ax.plot(dot[0], dot[1], 'ro', label='Dot')

# Check which area the dot is in
point = Point(dot)

if area1.contains(point) or area2.contains(point) or area3.contains(point) or area4.contains(point):
    print('O ponto está na Área A')

elif area5.contains(point) or area6.contains(point) or area7.contains(point) or area8.contains(point):
    print('O ponto está na Área B')

elif area9.contains(point):
    print('O ponto está na Área C')

elif area10.contains(point) or area11.contains(point):
    print('O ponto está na Área D')

elif area12.contains(point) or area13.contains(point):
    print('O ponto está na Área E')

else:
    print('O ponto está fora da região!')

# Adjust plot limits and display
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

ax.axhline(0, color='black', linewidth=1.5, linestyle='--')  # X-axis
ax.axvline(0, color='black', linewidth=1.5, linestyle='--')  # Y-axis

ax.legend()
plt.grid(True)
plt.show()
