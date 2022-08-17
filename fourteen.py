n = int(input('Enter the limit ?'))
n = n+1
limit = n
margin = n-1

for i in range(n):
    b = 0
    a = i
    for j in range(limit):
        if j >= margin:
            if a > 0 and b == 0:
                print(a,end=' ')
                a = a-1
            elif a==0 and b==0:
                print(a,end=' ')
                b=b+1
            else:
                print(b,end=' ')
                b=b+1
        else:
            print(' ',end=' ')
    print()
    limit=limit+1
    margin = margin-1

        
        
