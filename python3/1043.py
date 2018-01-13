a = list(map(float, input().split()))
p = (a[0] + a[1] + a[2]) / 2
if (((p - a[0]) * (p - a[1]) * (p - a[2])) > 0.0):
    print('Perimetro = {:.1f}'.format(p * 2))
else:
    print('Area = {:.1f}'.format((a[1] + a[0]) * a[2]/2))

