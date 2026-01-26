from sys import *

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
avg = 0
for i in range(n):
	cnt = 0
	sum = 0
	for j in range(i, n):
		sum += arr[j]
		cnt += 1
		if cnt >= k:
			avg = max(avg, sum / cnt)
print(avg)