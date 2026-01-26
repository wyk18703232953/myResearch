n,m=[int(x) for x in input().split()]
v=[]
h=[]
for i in range(n):
    x=int(input())
    v.append(x)
for i in range(m):
    x,y,z=[int(x) for x in input().split()]
    if x==1:
        h.append(y)
h.sort()
v.sort()
m=len(h)
n=len(v)
if n==0 or v[n-1]!=1000000000:
    v.append(1000000000)
    n+=1
mina=9999999999999
j=0
for i in range(n):
    while(j<m and h[j]<v[i]):
        j+=1
    #print(i+m-j)
    mina=min(mina,i+m-j)
print(mina)