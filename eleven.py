n = int(input('Enter a limit'))
c = 0
for i in range(1,n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        print(i+k,end=' ')
        c = i+k
    for t in range(1,i):
        c = c-1
        print(c,end=' ')
    print()