import math
for _ in range(1):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    ans=0
    for i in range(n):
	    c=0
	    sum1=0
	    for j in range(i, n):
		    sum1 += l[j]
		    c+=1
		    if c >= k:
			    ans=max(ans,sum1/c)
print(ans)    
                
            
        