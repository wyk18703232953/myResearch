n = int(input())
ar = [int(i) for i in input().split()]
ans = 0
for i in range(2*n):
    for j in range(i+1,2*n):
        if ar[i]==ar[j]:
            while j!=i+1:
                ar[j],ar[j-1]=ar[j-1],ar[j]
                j-=1
                ans+=1
print(ans)
		 				 			    		 	  		  	  		