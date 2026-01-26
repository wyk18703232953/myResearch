import bisect as bi
n,q = map(int,input().split())
a = list(map(int,input().split()))
l = list(map(int,input().split()))
som = sum(a)
e = 0
p = []
for i in a:
    e += i
    p.append(e)

e = 0
s = set(p)
for i in l:
    e += i
    if e >= som:
        e = 0

    x = bi.bisect(p,e)
    print(n-x)
