def check(n,p):
    k=str(n)
    k=k[::-1]
    s=0
    for j in range(len(k)):
        s+=(int(k[j])*(10**j-1))
    if s>=p:
        return 1
    else:
        return 0

n,s=map(int,input().split())
l=1
h=n
k=0
while(l<=h):
    m=(l+h)//2
    if check(m,s)==0:
        l=m+1
    else:
        h=m-1
    k+=1
print(n-l+1)
