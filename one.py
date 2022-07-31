input_a = int(input("enter a limit\n"))
print('*')
for i in range(1,input_a):
    a = 3*i
    for t in range(i):
        for k in range(i):
            print('*',end=' ')
        print()
    print()
    for j in range(a):
        if (j % 2 == 0):
            print('*',end=' ')
        else:
            print('$',end=' ')
    print()