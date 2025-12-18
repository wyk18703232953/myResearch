n=int(input())
l=list(map(int, input().split()))
r=list(map(int, input().split()))
maxx=0
s=[]
it=0
for i in range(n):
    s.append(l[i]+r[i])
    if l[i]>i or r[i]>n-i-1:
        it=1
its=list(s)
while maxx<n:
    summ=0
    ll=0
    rr=its.count(-1)
    for i in range(n):
        if its[i]==-1:
            ll+=1
            rr-=1
        if its[i]!=-1 and i<n-1 and r[i]<rr:
            it=1
            break
        if its[i]!=-1 and i>0 and l[i]<ll:
            it=1
            break    
    if it==1:
        break
    for i in range(n):
        if s[i]==maxx:
            s[i]=-maxx
            its[i]=-1
            summ+=1

    if summ==0:
        it=1
        break
    maxx+=summ
if it==1:
    print('NO')
else:
    print('YES')
    for i in s:
        print(i-min(s)+1, end=' ')
    