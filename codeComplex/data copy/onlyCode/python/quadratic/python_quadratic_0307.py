def helper(n,k,l):
	
	res = 0
	for i in range(n-k+1):
		base_seg = l[i:i+k]
		sm_bseg = sum(base_seg)
		ln_bseg = len(base_seg)
		ans = sm_bseg/ln_bseg

		for j in range(i+k,n):
			sm_bseg+=l[j]
			ln_bseg+=1
			ans=max(ans,sm_bseg/ln_bseg)


		res = max(res,ans)

	return res

n,k = map(int,input().split())
l = list(map(int,input().split()))

print(helper(n,k,l))