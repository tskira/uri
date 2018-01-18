for x in range(int(input())):
    a = int(input())
    if a == 0: print('NULL')
    else:
        print({1 : 'ODD', 0 : 'EVEN'}[a % 2], {0 : 'NEGATIVE', 1 : 'POSITIVE'}[a > 0])