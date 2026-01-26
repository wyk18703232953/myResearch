def gns():
    return  list(map(int,input().split()))
n=int(input())
ns=gns()
a='cslnb'
b='sjfnb'
ns.sort()
ans=[]
for i in range(1,n):
    if ns[i]==ns[i-1]:
        ans.append(i)
if len(ans)>=2 or sum(ns)==0:
    print(a)
    quit()
if len(ans)==1:
    i=ans[0]
    if ns[i]==0 or ns[i]-1 in ns:
        print(a)
        quit()
    r=sum(ns)-n*(n-1)//2
    if r%2==0:
        print(a)
        quit()
    else:
        print(b)
        quit()
else:
    r=sum(ns)-n*(n-1)//2
    if r%2==0:
        print(a)
        quit()
    else:
        print(b)

