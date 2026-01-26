n,l,r,x = [int(x) for x in input().split(" ")]
arr = [int(x) for x in input().split(" ")]
ans = 0
for i in range(2**n):
	subset = [] 
	for j in range(n): 
		if (i & (1 << j)) != 0: 
			subset.append(arr[j])
	if len(subset)>1:
	    mx = max(subset)
	    mn = min(subset)
	    sm = sum(subset)
	    if l<=sm<=r and mx-mn>=x:
	        ans+=1
print(ans)