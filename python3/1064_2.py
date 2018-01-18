a = [float(input()) for x in range(6)]
a.sort()
while(a[0] < 0):
    a = a[1:]
print('{} valores positivos\n{:.1f}'.format(len(a), sum(a)/len(a)))