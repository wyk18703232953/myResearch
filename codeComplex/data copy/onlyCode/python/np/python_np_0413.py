'''input
6 5
5 0 3 1 2
1 8 9 1 3
1 2 3 4 5
9 1 0 3 7
2 3 0 6 3
6 4 1 7 0
'''
# A coding delight
from sys import stdin, stdout
import gc
gc.disable()
input = stdin.readline
from collections import defaultdict


def check(num):
	bitmask = set()
	for i in range(n):
		b = 0
		for j in range(m):
			if arr[i][j] >= num:
				b ^= 1 << j
		bitmask.add(b)
	# print(num, bitmask)
	target = 2** m  - 1
	for i in bitmask:
		for j in bitmask:
			if i | j ==  target:
				return True
	return False


# main starts
n, m = list(map(int, input().split()))
arr = []
for _ in range(n):
	arr.append(list(map(int, input().split())))

# print(check(3))

start = 0
end = 10 ** 9
ans = -1
while start <= end:
	mid = (start + end) // 2
	if check(mid):
		ans = mid
		start = mid + 1
	else:
		end = mid - 1

bitmask = defaultdict(list)
for i in range(n):
	b = 0
	for j in range(m):
		if arr[i][j] >= ans:
			b  += 1<< j
	bitmask[b].append(i + 1)
target = 2 ** m - 1
for i in bitmask:
	for j in bitmask:
		if i | j == target:
			print(bitmask[i][0], bitmask[j][0])
			exit()
