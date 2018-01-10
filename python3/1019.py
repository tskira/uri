time = int(input())
time = divmod(time, 3600)
h = time[0]
time = divmod(time[1], 60)
print('%i:%i:%i' %(h, time[0], time[1]))