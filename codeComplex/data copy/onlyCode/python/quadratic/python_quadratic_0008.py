import math
n, r = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
ans = []
for i in range(n):
    t = r
    for j in range(i):
        a = abs(x[i] - x[j])
        if a <= 2 * r:
            t2 = (2 * r)**2
            t2 -= a**2
            t2 = math.sqrt(t2) + ans[j]
            t = max(t, t2)
    ans.append(t)
for k in ans:
    print(k)
	 				 			 		  			 				   					