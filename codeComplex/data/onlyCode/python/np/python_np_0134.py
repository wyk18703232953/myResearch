import sys

n = int(input())
l = list(map(int,input().split()))
c = list(map(int,input().split()))

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

a = {0:0}

for i in range(n):
    b = a.copy()
    for p in a.items():
        d = gcd(p[0], l[i])
        cost = p[1] + c[i]
        if d not in b: b[d] = cost
        elif b[d] > cost: b[d] = cost
    a = b

if 1 not in a: a[1] = -1
print(a[1])

                                                                                                         