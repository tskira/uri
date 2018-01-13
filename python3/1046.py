i, f = map(int, input().split())
total = f - i
if (total <= 0):
    total += 24
print('O JOGO DUROU {} HORA(S)'.format(total))