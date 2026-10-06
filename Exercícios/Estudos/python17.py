#h²= ca² + co²
ladoadj= float(input('Digite o lado do cateto adjacente:'))
ladooposto= float(input('Digite o lado do cateto oposto'))
import math
from math import sqrt
hipotenusa= (ladoadj) **2 + (ladooposto)**2
print(f'O comprimento da hipotenusa é {sqrt(hipotenusa)}')