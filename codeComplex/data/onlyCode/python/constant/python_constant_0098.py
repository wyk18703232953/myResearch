for x in range(int(input())):
	a,b = map(int,input().split())
	if a > b or a == b:c,d = a,b
	else:c,d = b,a
	e = [0]
	def fun(c,d):
		e[0] += c // d 
		f = d
		d = c % d
		c = f
		if f > 0 and d > 0:
			fun(c,d)
	fun(c,d)
	print(e[0])