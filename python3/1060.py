count = 0
for i in range(6):
    count += float(input()) > 0
print('{} valores positivos'.format(count))