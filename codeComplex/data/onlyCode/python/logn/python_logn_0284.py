n = [int(x) for x in input().split(' ')]
M = 1000000007

def a(k):
	M = 1000000007
	if(k>0):
		l = a(k//2)
		return (l*l*(k%2+1))%M
	else:
		return 1


if n[0]==0:
	print(0)
else:
	l = a(n[1])
	print((2*(n[0]%M)*l-l+1)%M)


