a = [float(input()) for x in range(6)]
s = 0.0
cont = 0
for x in a:
    if x > 0.0:
        s += x
        cont += 1
print('{} valores positivos\n{:.1f}'.format(cont, s/cont))