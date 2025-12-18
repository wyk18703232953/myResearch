n,s=map(int,input().split())
if s>=n:
	print(0)
else:
	ans=0
	def sod(n):
		s=str(n)
		ret=0
		for i in s:
			ret+=int(i)
		return ret 
	for nd in range(s,s+1000):
		if nd-sod(nd) >=s:
			ans+=1
		if nd==n:
			break
		if nd==(s+369):
			ans+=(n-nd)
			break 
	print(ans)