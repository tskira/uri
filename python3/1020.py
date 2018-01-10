tempo = int(input())
tempo = divmod(tempo, 365)
a = tempo[0]
tempo = divmod(tempo[1], 30)
print('%i ano(s)' %(a))
print('%i mes(es)' %(tempo[0]))
print('%i dia(s)' %(tempo[1]))