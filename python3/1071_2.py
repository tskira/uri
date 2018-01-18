maior, menor = (int(input()) for x in range(2))
if maior < menor: maior, menor = menor, maior
maior, menor = maior - 1 - (maior % 2), menor + 1 + (menor % 2)
print(int((maior ** 2 + 2 * (maior + menor) - menor ** 2) / 4))