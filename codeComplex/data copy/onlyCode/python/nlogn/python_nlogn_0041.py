n=int(input())
a=list(map(int,input().split()))
temp=max(a)
if len(set(a))==1 and a[0]==1:
    print(*a[:-1],2)
else:
    a[a.index(temp)]=1
    a.sort()
    print(*a)