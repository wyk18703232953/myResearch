from collections import Counter
mp = Counter()
n = int(input())
arr = list(map(int,input().split()))

tot , cnt, ans = 0, 0, 0
for i in arr:
	ncnt = cnt - mp[i] - mp[i+1] - mp[i-1]
	ntot = tot - (i * mp[i]) - ((i-1)*mp[i-1]) - ((i+1)*mp[i+1])
	nsum = (ncnt * i) - ntot
	ans += nsum
	mp[i] += 1
	cnt += 1
	tot += i
print(ans)
