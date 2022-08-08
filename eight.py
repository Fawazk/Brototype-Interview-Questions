a = 1
for i in range(1,4):
    for j in range(i):
        print(i)
    for k in range(i+1):
        print(a,end=' ')
        a = a+1
    print()