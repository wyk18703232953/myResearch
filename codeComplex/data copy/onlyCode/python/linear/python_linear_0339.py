# https://codeforces.com/problemset/problem/1004/A

import math

n, d = [int(x) for x in input().split(' ')]
pos = [int(x) for x in input().split(' ')]

# med = []
# for i in range(1,n+1):
# 	med.append((pos[i-1] + pos[i]) / 2)

# sx = [x - d for x in pos]
# dx = [x + d for x in pos]

# print(med)


count = 2

for i in range(1,n):
	if math.fabs(pos[i] - pos[i-1]) > 2*d:
		count += 2
	elif math.fabs(pos[i] - pos[i-1]) == 2*d:
		count += 1
	else:
		continue;

print(count)
