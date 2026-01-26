n = int(input())
l = list(map(int,input().split()))
i = 0
p = []
while 2**i <= 10**18:
    p.append(2**i)
    i = i+1

d = {}
s = set()
for i in l:
    s.add(i)
    if i in d:
        d[i] += 1

    else:
        d[i] = 1

z = set()
for i in s:
    f = 1
    for j in p:
        e = j-i
        if e in s:
            if e == i and d[e] == 1:
                continue

            f = 0
            break

    if f:
        z.add(i)

ans = 0
for i in z:
    ans += d[i]

print(ans)