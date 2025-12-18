n = int(input())-1
c = 0
for i in range(11):
	c += 9*(i+1)* 10**i
	if c > n:
		n -= (c - 9*(i+1)* 10**i)
		v = n // (i+1)
		print(str(10**i + v)[n%(i+1)])
		break
