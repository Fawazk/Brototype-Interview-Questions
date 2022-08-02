n = int(input('enter the limit'))
a = 0
for i in range(n):
    for j in range(n):
        if j>=a:
            if i%2==0:
                print('$',end=' ')
            else:
                print("*",end=' ')
        else:
            print(' ',end=' ')
    a = a + 1
    print()