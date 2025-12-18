n,k=map(int, input().split())
a=list(map(int, input().split()))
i=0
d=0
x=-1
y=-1
s=[0]*(10**5+1)
for j in range (len(a)):
    s[a[j]]+=1
    i+=1
    if s[a[j]]==1:
        d+=1
    if i==1:
        x=j+1
    if d==k:
        y=j+1
        break
while k!=1 and s[a[x-1]]-1!=0:
    s[a[x-1]]-=1
    x+=1
if x==-1 or y==-1:
    x=-1
    y=-1
print(x,y)