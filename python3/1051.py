s = float(input())
a = [0 for x in range(3)]
if (s <= 2000.00):
    print('Isento')
else:
    s -= 2000.0
    if (s - 1000.00 <= 0):
        a[0] = s
    else:
        a[0] = 1000.00
        s -= 1000.00
        if (s - 1500.00 <= 0):
            a[1] = s
        else:
            a[1] = 1500.00
            s -= 1500.00
            a[2] = s
    print('R$ {:.2f}'.format(a[0] * 0.08 + a[1] * 0.18 + a[2] * 0.28))