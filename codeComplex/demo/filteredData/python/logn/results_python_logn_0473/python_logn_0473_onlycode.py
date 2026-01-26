print("? 0 0", flush=True)
res = input()
i = 1
a = 0
b = 0
for i in range(29,-1,-1):
	print("?",(a^(1<<i)), b, flush=True)
	res1 = input()
	print("?",a, (b^(1<<i)), flush=True)
	res2 = input()
	if res1 == res2:
		if res == '1':
			a ^= (1<<i)
		else:
			b ^= (1<<i)
		res = res1
	elif res1 == '-1':
		a ^= (1<<i)
		b ^= (1<<i)
print("!", a, b, flush=True)