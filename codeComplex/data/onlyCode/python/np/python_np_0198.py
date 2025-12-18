def check(j):
    if sum(j)>=l and sum(j)<=r and (max(j)-min(j))>=x:
        return 1
    return 0
        

from itertools import combinations
n,l,r,x=list(map(int,input().split()))
c=list(map(int,input().rstrip().split()))
count=0
for i in range(2,n+1):
    a=list(combinations(c,i))
    for j in a:
        
        if check(j):
            count+=1
print(count)
        
    
    
				 	 	 	  	 	   		   			   		