n=int(input())
a=list(map(int,input().split()))
a.sort()
if a[n-1]==1:
    a[n-1]+=1
else:
    a[n-1]=1
a.sort()
print(*a)
