n=int(input())
l=list(map(int,input().split()))
r=list(map(int,input().split()))
if l[0]!=0 or r[n-1]!=0:
    print("NO")
    exit(0)
s=[(l[i]+r[i]) for i in range(n)]
m=max(s)+1
k=[]
for i in s:
    k.append(m-i)
l1=[]
r1=[]

for i in range(n):
    c=0
    d=0
    for j in range(0,i):
        if k[j]>k[i]:
            c+=1
    l1.append(c)
    for j in range(i+1,n):
        if k[j]>k[i]:
            d+=1
    r1.append(d)
if l1!=l or r1!=r:
    print("NO")
else:
    print("YES")
    print(*k)
        
    
    

    