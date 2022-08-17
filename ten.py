
n = 11
a = int(n/2)
j = 0
count = 0
print(a)
for i in range(n):
    if count < n/2:
        for j in range(i):
            if j % 2 == 0:
                    print('*',end=' ')
            else:
                print('^*',end=' ')
        count = count +1
        print()
    else:
        for k in range(a):
            if k % 2 == 0:
                print('*',end=' ')
            else:
                print('^*',end=' ')
        a = a-1
        print()
