n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = {}
i = 1
for x in arr:
	if len(d) == m:
		break
	d[x] = i
	i += 1
if len(d) == m:
	print(min(d.values()), max(d.values()))
else:
	print(-1,-1)
