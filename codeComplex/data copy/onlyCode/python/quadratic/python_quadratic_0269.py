n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
l=[]
for i in range(m):
    if y[i] in x:
        l.append(x.index(y[i]))
l.sort()
for i in l:
    print(x[i],end=" ")