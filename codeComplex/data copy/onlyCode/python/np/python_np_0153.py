n, l, r, x = map(int, input().split())
a = [int(i) for i in input().split()]

count = 0
for i in range(1, 2**n+1):
	temp = []
	for j in range(n):
		if i & (1 << j):
			temp.append(a[j])

	if len(temp) and max(temp) - min(temp) >= x and sum(temp) >= l and sum(temp) <= r:
		count += 1

print(count)