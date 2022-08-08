
n = int(input('enter odd number as limit'))
if n % 2 == 0:
    n = int(input('you entered a even number pls enter a odd number'))
for i in range(n):
    for k in range(i):
        print('*',end=' ')
    print()
    for j in range(n):
        print('*',end=' ')
    n = n - 1
    print()
