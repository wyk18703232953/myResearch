n, pos, a, b = map(int,input().split())

lf, rf = a - 1, n - b
if lf == rf == 0:
	print("0")
elif lf == 0:
	print(abs(pos-b)+1)
elif rf == 0:
	print(abs(pos-a)+1)
else:
	cl = abs(a-pos) + 1
	cr = abs(b-pos) + 1
	xn = abs(a-b) + 1
	if cl < cr:
		print(cl+xn)
	else:
		print(cr+xn)