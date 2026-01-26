l,r = map(int,input().split())

a = "{0:062b}".format(l)
b = "{0:062b}".format(r)

n = len(a)
i = 0

if (l == r):
    print(0)
else:
    while (i<n and a[i] == b[i]):
        i += 1
    print(2**(62-i) - 1)