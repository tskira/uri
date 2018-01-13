entry = list(map(int, input().split()))
ordenado = entry[:]
ordenado.sort()
ordenado.append('')
ordenado.extend(entry)
for i in range(len(ordenado)):
    print(ordenado[i])