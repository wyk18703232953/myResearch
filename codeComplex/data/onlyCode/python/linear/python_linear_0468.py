a=input()
n=len(a)
b=[]
c=0
d=0
for i in range(1,n):
    if a[i]==a[i-1]:
        b.append(['bw'.find(a[c]),i-c])
        d=max(d,i-c)
        c=i
b.append(['bw'.find(a[c]),n-c])
d=max(d,n-c)
if d<n and b[0][0]==(b[-1][0]+b[-1][1])%2:
    d=max(d,b[-1][1]+b[0][1])
print(d)