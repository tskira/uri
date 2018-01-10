a, b, c, d = map(int, input().split())

if (b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and not(a & 1)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
