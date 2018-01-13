a = list(map(int, input().split()))
a.sort()
if(a[1] % a[0]):
    print('Nao sao Multiplos')
else:
    print('Sao Multiplos')