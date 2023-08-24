import math

a = 2
b = 2
c = -6

if a > 0:
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print('As Raizes são:', x1, 'e', x2)

    else:
        print('A equação não tem Raizes Reais.')
else:
    print('O coeficiente A não é positivo. A equação não é quadratica')