a = [0 for i in range(100)]
b = [0 for i in range(100)]
for i in range(1, 100):
	a[i] = a[i - 1] * 2 + 1
	b[i] = b[i - 1] + a[i]
def calc(x):
	return (4 ** x - 1) // 3
for i in range(int(input())):
	n, k = map(int, input().split())
	if n > 35:
		print("YES " + str(n - 1))
	elif 1 + calc(n - 1) >= k:
		print("YES " + str(n - 1))
	elif calc(n) < k:
		print("NO")
	else:
		for i in range(1, (n + 1)):
			if b[i] <= k and k <= calc(n) - (2 ** (i + 1) - 1) * calc(n - i):
				print("YES " + str(n - i))
				break
		else:
			print("NO")