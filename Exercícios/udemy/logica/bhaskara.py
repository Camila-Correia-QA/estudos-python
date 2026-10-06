# ax² + bx + c = 0
# x = -b +- √delta / 2a
#delta = b² - 4ac
import math

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
delta = ((b )** 2) - (4 * a * c)
print(delta)
if delta < 0 or a == 0:
    print ("Essa equação não possui raízes reais" )

elif delta == 0:
    print ("O valor da raiz é:" + str(raiz))
    raiz = ((-1 * (b)) + math.sqrt(delta)) / (2 * a)
    raiz2 = ((-1 * (b)) - math.sqrt(delta)) / (2 * a)

elif delta > 0:
    raiz = ((-1 * (b)) + math.sqrt(delta)) / (2 * a)
    raiz2 = ((-1 * (b)) - math.sqrt(delta)) / (2 * a)
    print (f' O valor das raízes é: {(raiz):.2f} e {(raiz2):.2f}')
