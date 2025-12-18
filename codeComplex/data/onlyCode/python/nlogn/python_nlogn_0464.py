def max_profit(n,k,l,d):
    a=[]
    s,p,i=0,0,-1
    while(len(a)!=k-1):
        p+=1
        i+=1
        if l[i] in d:
            s+=l[i]
            a.append(p)
            p=0
            d.remove(l[i])
    print(s+d[0])
    a.append(n-sum(i for i in a))
    print(*a)


n,k=map(int,input().split())
l=list(map(int,input().split()))
m=[]
m[:]=l[:]
d=[]
m.sort(reverse=True)
for i in range(k):
    d.append(m[i])
max_profit(n,k,l,d)