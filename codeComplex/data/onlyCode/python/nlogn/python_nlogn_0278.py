n = int(input())
d = {}
for i in range(n):
    a,b = map(int,input().split())
    d[a] = b
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    if d.get(a)==None:
        d[a] = b
    else:
        if b>d[a]:
            d[a] = b
ans = 0
for i in d:
    ans+=d[i]
print(ans)
