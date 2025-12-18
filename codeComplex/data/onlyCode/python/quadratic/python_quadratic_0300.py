n=int(input())
a=list(map(int,input().split()))
ans=0
while len(a)>0:
    c=a.pop(0)
    i=a.index(c)
    ans+=i
    del a[i]
print(ans)