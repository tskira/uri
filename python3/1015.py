a1 = tuple(map(float, input().split()))
a2 = tuple(map(float, input().split()))
print('%.4f' %(((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5))