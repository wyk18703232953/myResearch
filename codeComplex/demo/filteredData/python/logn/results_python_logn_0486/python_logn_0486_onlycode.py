#q = int(input())
q = 1
for t in range(q):
	k = int(input())
	m = 0
	p = 9
	while k > p:
		m = m+1
		l = p
		p = p+ 9*(10**m)*(m+1)
	if m == 0:
		print(k)
		continue
	ans = int("9"*m)+ (k-l)//(m+1)
	if (k-l)%(m+1) == 0:
		print(str(ans)[-1])
	else:
		ans = ans+1
		print(str(ans)[((k-l)%(m+1))-1])