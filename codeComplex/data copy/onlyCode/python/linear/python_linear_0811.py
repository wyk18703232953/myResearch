n = int(input())
a = list(map(int, input().split()))
d = {}
for ai in a:
	if ai in d:
		d[ai] += 1
	else:
		d[ai] = 1
if max(d.values()) >= 3 or 0 in d and d[0] >= 2 or list(d.values()).count(2) >= 2:
	print('cslnb')
	exit()
for i in d:
	if d[i] == 2 and i - 1 in d:
		print('cslnb')
		exit()
s = sum(a)
if s >= n * (n - 1) // 2:
	if (s - n * (n - 1) // 2) % 2 == 0:
		print('cslnb')
	else:
		print('sjfnb')
else:
	pass

