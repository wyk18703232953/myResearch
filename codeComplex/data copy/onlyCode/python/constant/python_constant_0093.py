for _ in range(int(input())):
	a, b = map(int, input().split())
	result = 0
	while min(a, b)!=0:
		x = max(a, b)
		y = min(a, b)
		a = x
		b = y
		result+=a//b
		a%=b
	print(result)