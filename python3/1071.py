a = [int(input()) for x in range(2)]
a.sort()
x = [x for x in range(a[0], a[1] + 1)]
x = [i for i in x[1:-1] if i % 2 == 1]
print(sum(x))