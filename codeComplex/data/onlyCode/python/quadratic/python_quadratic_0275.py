a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
for i in c:
    if i in d:
        e.append(i)
for j in e:
    print(j,end=" ")