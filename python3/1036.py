a, b, c = map(float, (input().split()))

if(a):
    delta = b ** 2 - (4 * a * c)
    if(delta >= 0):
        delta **= 0.5
        print('R1 = %.5f' %((-b + delta) / (2 * a)))
        print('R2 = %.5f' %((-b - delta) / (2 * a)))
    else:
        print('Impossivel calcular')
else:
    print('Impossivel calcular')