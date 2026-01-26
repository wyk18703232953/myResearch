n,l,r,x=map(int,input().split())
import math
z=list(map(int,input().split()))
count=0
for i in range(pow(2,len(z))):
    
    mini=math.inf
    maxa=0
    j=i
    inde=0
    sume=0
    while(j>0):
        
        if(j&1):
            sume+=z[inde]
            maxa=max(maxa,z[inde])
            mini=min(mini,z[inde])
        j=j>>1
        inde+=1

    if(maxa-mini>=x and l<=sume<=r):
        count+=1
    
print(count)
        
        
