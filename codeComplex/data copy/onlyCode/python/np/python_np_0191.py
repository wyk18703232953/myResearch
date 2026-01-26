n, l, r, x = map(int, input().split())
d = list(map(int, input().split()))
ans = 0
for i in range(pow(2, n)-1, -1, -1):
	s = bin(i)[2:]
	while(len(s) < n):
		s = "0"+s
	diff = 0
	t = []
	for j in range(n):
		if(s[j]=='1'):
			diff += d[j]
			t.append(d[j])
	t.sort()
	# print(s, t)
	if(l <= diff <= r and t[-1]-t[0] >= x):
		ans += 1
print(ans)