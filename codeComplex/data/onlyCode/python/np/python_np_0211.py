n,l,r,x = map(int,input().split())
a = list(map(int,input().split()))
count=0
for i in range(2**n):
    maxc=-1
    minc=-1
    c=0
    for j in range(n):
        if i>>j&1==1:
            c+=a[j]
            maxc=max(maxc,a[j])
            if minc==-1:
                minc=a[j]
            else:
                minc=min(a[j],minc)
    if c>=l and c<=r and maxc - minc >=x:
        count+=1
print(count)

