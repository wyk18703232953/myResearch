l, r = [int(x) for x in input().split()]

r = bin(r)[2:]
l = bin(l)[2:]

r = r[::-1]
l = l[::-1]

if l == r:
    print(0)
else:

    l += '0' * (len(r) - len(l))
    p = -1
    for i in range(len(r)):
        if r[i] != l[i]:
            p = i

    a = '1' * p + '0'
    b = '0' * p + '1'

    print(int(a, 2) ^ int(b, 2))
