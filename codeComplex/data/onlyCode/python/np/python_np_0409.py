import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
def bs(a,mid,ans):
    global n,m
    can=[0 for i in range(1<<m)]
    for i in range(n):
        t=0
        for j in range(m):
            t=(t<<1)|(a[i][j]>=mid)
           
        can[t]=i+1
    #print(can)    
    for i in range(1<<m):
        if(not can[i]):
            continue
        for j in range(1<<m):
            if not can[j]:
                continue
            if i|j==(1<<m)-1:
                #print(i,j)
                ans[0]=can[i]
                ans[1]=can[j]
                return 1
    return 0            
                
for i in range(n):
    p=[int(x) for x in input().split()]
    a.append(p)
l=0
r=100000000000
ans=[1,1]
while l<=r:
    mid=(l+r)//2
    if bs(a,mid,ans):
        l=mid+1
    else:
        r=mid-1
    #print(l,r,ans,mid)    
print(*ans)        
        
    