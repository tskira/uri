abc = tuple(map(float, input().split()))

print('TRIANGULO: %.3f' %(abc[0] * abc[2] / 2))
print('CIRCULO: %.3f' %(3.14159 * (abc[2] ** 2)))
print('TRAPEZIO: %.3f' %((abc[0] + abc[1]) * abc[2] / 2))
print('QUADRADO: %.3f' %(abc[1] ** 2))
print('RETANGULO: %.3f' %(abc[0] * abc[1]))

