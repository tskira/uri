v = float(input())
rise = {0 : .15, 1 : .12, 2 : .10, 3 : .07, 4 : .04}
if( v <= 400.00):
    r = 0
elif( v <= 800.00):
    r = 1
elif( v <= 1200.00):
    r = 2
elif( v <= 2000.00):
    r = 3
else:
    r = 4
percent = rise[r] * v
print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:d} %'.format(v + percent, percent, int(rise[r] * 100)))