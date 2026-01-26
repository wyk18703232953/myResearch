from sys import stdin,stdout
n,q=map(int,input().split())
mod=1000000007
o=[]
s=[]
r=m=0
a=input()
for i in a:
    if i=='0':
        r+=1
    else:
        m+=1
    o.append(r)
    s.append(m)
z=[1]
#print(o)
for i in range(100000):
    z.append((z[-1]*2)%mod)
for j in range(q):
    l,r=(int(j) for j in stdin.readline().split())
    m=r-l+1
    zs=o[r-1]-o[l-1]+(a[l-1]=='0')
    os=m-zs
    #print(zs,os)
    if zs!=0:
        print((((z[os]-1)%mod)*((z[zs])%mod))%mod)
    else:
        print(((z[os]-1)%mod))
    
    
    
