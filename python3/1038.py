c, q = map(int, input().split())
valores = {1 : 4.00, 2 : 4.5, 3 : 5.0, 4 : 2.0, 5 : 1.5}
print('Total: R$ %.2f' %(q * valores[c]))