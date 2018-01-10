notas = list(map(float, input().split()))
for i in range(4):
    notas[i] *= (((i + 1) % 4) + 1)
media = sum(notas)/10.0
print('Media: %.1f' %(media))
if (media >= 7.0):
    print('Aluno aprovado.')
elif(media < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: %.1f' %(exame))
    media += exame
    media /= 2
    if(media >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' %(media))