n, l, r, x = list(map(int, input().split()))
s = list(map(int, input().split()))
olmps = []
c = []
v = 0
for i in range(1<<n):
    olmps.append([])
    for j in range(n):
        if i & (1<<j):
            olmps[-1].append(s[j])
for o in olmps:
    if l <= sum(o) <= r:
        c.append(o)
for z in c:
    if max(z) - min(z) >= x:
        v+=1
print(v)
