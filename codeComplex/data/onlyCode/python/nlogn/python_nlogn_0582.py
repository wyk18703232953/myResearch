
n=int(raw_input())

ans=[]
p=1
fin=n
while len(ans)<n-1:
	for i in range(fin-(n/(2**p))):
		ans.append(2**(p-1))
		fin-=1
	p+=1

if 2**(p-2) + 2**(p-1) <=n:
	ans.append(2**(p-1) + 2**(p-2))
else:
	ans.append(2**(p-1))

s=" ".join(str(x) for x in ans)

print(s)
