def get_sign_1(fo):
	def res(s, f=fo):
		if f**2+s**2 == 2*f*s+1:
			return '1'
		else:
			return '0'
	return res


def get_signs_2(cf, rev):
	cf -= 1
	if rev:
		def res(fo, cff=cf):
			if fo >= cff:
				def res2(s, f=fo):
					if s == f:
						return '0'
					elif s >= cff:
						return '0'
					else:
						return '1'
			else:
				def res2(s, f=fo):
					if s == f:
						return '0'
					else:
						return '1'
			return res2
	else:
		def res(fo, cff=cf):
			if fo >= cff:
				def res2(s, f=fo):
					if s == f:
						return '0'
					elif s >= cff:
						return '1'
					else:
						return '0'
			else:
				def res2(s):
					return '0'
			return res2
	return res
n, a, b = map(int, input().split())
c = a*b
if a+b == c+1 and (c > 1 or n == 1 or n > 3):
	print("YES")
	if c == 1:
		get_sign_f = get_sign_1
	else:
		get_sign_f = get_signs_2(c, c == b)
	for foo in range(n):
		print(''.join(map(get_sign_f(foo), range(n))))
else:
	print("NO")
