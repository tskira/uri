x, y = map(float, (input().split()))
quadrantes = {(True, True) : 'Q1', (True, False) : 'Q4', (False, True) : 'Q2', (False, False) : 'Q3'}
eixos = {(True, True): 'Origem', (True, False) : 'Eixo Y', (False, True) : 'Eixo X'}
zero = tuple(map(lambda x: x == 0, [x, y]))
if(zero in eixos.keys()):
    print(eixos[zero])
else:
    print(quadrantes[tuple(map(lambda x: x > 0 , [x, y]))])