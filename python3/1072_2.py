n = int(input())
count = 0
for x in range(n):
    count += 10 <= int(input()) <= 20
print('{} in\n{} out'.format(count, n - count))