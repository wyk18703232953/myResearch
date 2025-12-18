from collections import defaultdict as di

n = int(input())
a = list(map(int, input().split()))
d = di(int)
res, sum = 0, 0
for i in range(n):
	res += a[i] * i - sum - d[a[i]-1] + d[a[i]+1]
	sum += a[i]
	d[a[i]] += 1
print(res)