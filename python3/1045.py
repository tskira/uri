a = list(map(float, input().split()))

a.sort(reverse = True)

a2, b2, c2 = map(lambda x: x**2, (a))

if (a[0] >= (a[1] + a[2])):
    print('NAO FORMA TRIANGULO')
else:
    if (a2 == b2 + c2):
        print('TRIANGULO RETANGULO')
    else:
        if (a2 > (b2 + c2)):
            print('TRIANGULO OBTUSANGULO')
        elif (a2 < (b2 + c2)):
            print('TRIANGULO ACUTANGULO')
    if (a[0] == a[1] == a[2]):
        print('TRIANGULO EQUILATERO')
    elif (a[0] == a[1] or a[1] == a[2] or a[0] == a[2]):
        print('TRIANGULO ISOSCELES')