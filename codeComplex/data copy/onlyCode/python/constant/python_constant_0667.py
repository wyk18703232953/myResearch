print("? 0 0")
ans00 = input()
xr = 0
a = 0
b = 0
cb = 2 ** 29
while cb:
	print("?", xr + cb, cb)
	ans11 = input()
	print("?", xr, cb)
	if ans11 == ans00:
		ans01 = input()
		if ans01 == '1':
			a += cb
			b += cb
	else:
		ans00 = input()
		if ans11 == '1':
			b += cb
		else:
			a += cb
		xr += cb
	cb //= 2
print("!", a, b)
