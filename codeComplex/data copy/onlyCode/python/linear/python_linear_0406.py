n = int(input())
m = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

low = 1
high = 1000000000
ans = -1

while low<=high:
	if high-low < 0.000001: low = high 
	mid = low+(high-low)/2
	try_val = mid
	init_wt = m+try_val
	isPossible = True
	for i in range(n):
		req1 = init_wt/a[i]
		try_val -= req1
		if try_val<=0: 
			isPossible = False
			break
		j=(i+1)%n
		init_wt -= req1
		req2 = init_wt/b[j]
		try_val -= req2
		if try_val<0 or (i<n-1 and try_val==0): 
			isPossible = False
			break
		init_wt -= req2
	if isPossible:
		ans = mid
		high = mid-0.000001
	else: low = mid+0.000001

if (ans==-1):
	isPossible = True
	try_val = 1000000000.000001
	init_wt = m+try_val
	for i in range(n):
		req1 = init_wt/(a[i])
		try_val -= req1
		if try_val<=0:
			#print("lol") 
			isPossible = False
			break
		j=(i+1)%n
		init_wt -= req1
		req2 = init_wt/(b[j])
		try_val -= req2
		if try_val<0 or (i<n-1 and try_val==0): 
			isPossible = False
			break
		init_wt -= req2
	if isPossible: ans = 1000000000
print(ans)