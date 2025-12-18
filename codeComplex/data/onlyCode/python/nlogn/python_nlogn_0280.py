


n = int(input())
d={}
for _ in range(n):
    a,b = map(int,input().split())
    d[a] = b

s=0
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())

    if x in d:
        d[x] = max(d[x],y)

    else:
        d[x] = y

for i in d:

    s+=d[i]
print(s)

