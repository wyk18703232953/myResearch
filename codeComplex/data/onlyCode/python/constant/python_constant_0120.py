n=int(input())
l=list(str(n))
if n>=0:
	print(n)
else:
	if int(l[-1])>int(l[-2]):
		l.pop(-1)
	else:
		l.pop(-2)
	print(int(''.join(l)))
