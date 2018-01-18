a = [int(input()) for x in range(5)]
impar = sum(map(lambda x: x % 2, a))
positivo = sum(map(lambda x: x > 0, a))
negativo = 5 - a.count(0) - positivo
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'
      .format(5 - impar, impar, positivo, negativo))