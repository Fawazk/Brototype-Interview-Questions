
n = int(input("Enter the limit ?"))
dupn=n
limit = 0
for i in range(n*2):
    if limit == 0 and dupn != 0:
        for j in range(dupn):
            if j % 2 == 0:
                print('*',end='')
            else:
                print('-',end='')
        dupn = dupn-1
        print()
    elif limit == 0:
        limit = 2
    else:
        for k in range(limit):
            if k % 2 == 0:
                print('*',end='')
            else:
                print('-',end='')
        limit = limit+1
        print()
        