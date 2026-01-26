a,b,c,d,e,f=list(map(int,input().split()))
n,n2=1,a*b+c*d+e*f
while n**2<n2:
    n+=1
if n**2>n2:
    print(-1)
    exit()
l=sorted([[max(a,b),min(a,b),'A'],[max(c,d),min(d,c),'B'],[max(e,f),min(e,f),'C']])
if l[2][0]!=n:
    print(-1)
    exit(0)
v=str(n)+'\n'+(l[2][2]*n+'\n')*l[2][1]
if l[0][0]==n and l[1][0]==n:
    for i in range(2):
        v+=(l[i][2]*n+'\n')*l[i][1]
else:
    s=n-l[2][1]
    if s not in l[0] or s not in l[1]:
        print(-1)
        exit()
    if s!=l[0][0]:
        l[0][0],l[0][1]=l[0][1],l[0][0]
    if s!=l[1][0]:
        l[1][0],l[1][1]=l[1][1],l[1][0]
    v+=(l[0][2]*l[0][1]+l[1][2]*l[1][1]+'\n')*s
print(v)
