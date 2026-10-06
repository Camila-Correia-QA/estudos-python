def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0]
dobra(valores)
print(valores)


def soma(a,b,c):
    s= a + b + c
    print(s)


soma(4,5,2)
soma(8,9,2)

def contador(*núm):
    print(núm)


