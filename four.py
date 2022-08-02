n = int(input('enter the limit\n'))
b = n-2
for i in range(n):
    a = b
    for j in range(n):
        if j > a:
            if n % 2 != 0:
                if i % 2 == 0:
                    if j % 2 == 0:
                        print('*',end=" ")
                    else:
                        print('$',end=" ")
                else:
                    if j % 2 == 0:
                        print('$',end=" ")
                    else:
                        print('*',end=" ")
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        print('$',end=" ")
                    else:
                        print('*',end=" ")
                else:
                    if j % 2 == 0:
                        print('*',end=" ")
                    else:
                        print('$',end=" ")
            a = a-1
        else:
            print(' ',end=' ')
    b = b-1
    print()