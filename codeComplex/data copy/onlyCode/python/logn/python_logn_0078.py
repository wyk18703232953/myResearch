l, r = map(int, input().split(' '))
n1 = bin(l)[2:]
n2 = bin(r)[2:]
if l==r:
    print(0)
elif len(n1) < len(n2):
    print(int(len(n2)*'1', 2))
else:
    index = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            index = i
            break
    print(int((len(n1)-index)*'1', 2))
        