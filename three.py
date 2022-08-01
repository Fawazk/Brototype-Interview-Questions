for i in range(5):
    a = 2*i
    b = i
    while b >= 0 and i % 2 == 0:
        print("*",end=' ')
        b=b-1
    print()
    for j in range(a):
        print("$ *",end=' ')
    print()
