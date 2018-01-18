# esse codigo poderia funcionar, mas acredito que o uri envia numeros repetidos entao nao funfa
n = int(input())
a = set([int(input()) for x in range(n)])
i = set([x for x in range(10, 21)])
fora = len(a - i)
print('{} in\n{} out'.format(n - fora, fora))