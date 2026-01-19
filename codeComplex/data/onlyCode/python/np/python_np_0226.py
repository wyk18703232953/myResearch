from itertools import combinations
 
n, l, r, x = map(int, input().split())
(*a,) = map(int, input().split())
sumu = 0
for i in range(2, n + 2):
    for j in combinations(a, i):
        if (r >= sum(j) >= l) and (max(j) - min(j) >= x):
            sumu += 1
print(sumu)
	 		      	 	  		   	  		 	 	