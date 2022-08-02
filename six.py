alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = int(input('enter the limt'))
count = 0
for i in range(n):
    for j in range(i):
        if count < len(alphabet):
            print(alphabet[count],end="")
            count += 1
    print()