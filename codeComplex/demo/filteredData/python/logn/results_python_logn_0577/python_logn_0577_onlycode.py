n = int(input())
i = 0
s = 0
while True:
	temp = (i+1)*9*(10**i)
	if s + temp <= n:
		s += temp
		i += 1
	else:
		break
tc = n - s

nd = tc//(i+1) - 1
tc -= (nd+1)*(i+1)
f = 10**i + nd
if tc != 0:
	print(str(10**i+nd+1)[tc-1])
else:
	print(str(10**i+nd)[-1])
