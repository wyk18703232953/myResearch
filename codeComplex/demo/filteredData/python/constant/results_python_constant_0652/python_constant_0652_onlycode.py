a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a,b,c= sorted([a,b,c])

path = []
for i in range(min(a[1],b[1],c[1]) , max(a[1],b[1],c[1]) + 1):
    path.append((b[0],i))
for i in range(a[0],b[0]+1):
    path.append((i,a[1]))
for i in range(b[0],c[0]+1):
    path.append((i,c[1]))

print(len(set(path)))
for i in set(path):
    print(*i)
