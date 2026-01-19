def GSB(x):
	counter=0
	while x!=0:
		counter+=1
		x=x>>1
	return counter
	
problems,minimum,maximum,difference=[int(x) for x in input().split()]
array=[int(x) for x in input().split()]
combinations=[int(x) for x in range(2**problems)]
total=0

for i in combinations:
	checker=[x for x in array]+['a']
	j=0
	z=GSB(i)
	check=1
	while j!=z and i!=0:
		if i&1==1:
			checker[j]='a'
			check+=1
		i=i>>1
		j+=1
	for i in range(check):
		checker.remove('a')
	checker.sort()
	if minimum<=sum(checker)<=maximum and len(checker)>=2 and checker[-1]-checker[0]>=difference:
		total+=1
print(total)