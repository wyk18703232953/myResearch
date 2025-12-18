def max_profit(n,k,l,d):
    a=[]
    p,i=0,-1
    while(len(a)!=k-1):
        p+=1
        i+=1
        if l[i] in d:
            a.append(p)
            p=0
            d.remove(l[i])
    a.append(n-sum(a))
    print(*a)


n,k=map(int,input().split())
l=list(map(int,input().split()))
d=sorted(l,reverse=True)[:k]
print(sum(d))
max_profit(n,k,l,d)