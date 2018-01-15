hi, mi, hf, mf = map(int, input().split())
totalh = hf - hi
totalm = mf - mi

if (totalh <= 0):
    totalh += 24
if (totalm < 0):
        totalm += 60
        totalh -= 1
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(totalh, totalm))