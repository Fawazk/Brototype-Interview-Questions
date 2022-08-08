
n = 10
a = n*2-1
b = 0
for i in range(n):
    for j in range(n*2):
        if b < j and a > j:
            print('&',end='') 
        else:
            print('*',end='')
    b = b+1
    a = a-1
    print()