a = [input().split() for x in range(4)]
dia = int(a[2][1]) - int(a[0][1])
hora = int(a[3][0]) - int(a[1][0])
minuto = int(a[3][2]) - int(a[1][2])
segundo = int(a[3][-1]) - int(a[1][-1])

if (hora < 0):
    hora += 24
    dia -= 1
if (minuto < 0):
    minuto += 60
    hora -= 1

if (segundo < 0):
    segundo += 60
    minuto -= 1

print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dia, hora, minuto, segundo))