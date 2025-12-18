#greedy is wrong due to the constraint ki do alag se uthenge, so youd also want to keep 2 ppl above 0

#yeh dp se hoga, clear hai

import sys

def input():
	return sys.stdin.readline().rstrip()

def input_split():
	return [int(i) for i in input().split()]

# testCases = int(input())
# answers = []
# for _ in range(testCases):
	#take input
x, y, z  = input_split()
arr_x = input_split()
arr_y = input_split()
arr_z = input_split()

x += 1
y += 1
z += 1

lengths = [x,y, z]
arrs = [arr_x, arr_y, arr_z ]

for a in arrs:
	a.sort()
	# a.reverse()

dp = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]

for i in range(1,x):
	for j in range(1,y):
		# if i!= 0 and j!= 0:
		dp[i][j][0] = dp[i-1][j-1][0] + arr_x[i-1]*arr_y[j-1]

for j in range(1, y):
	for k in range(1, z):
		# if j!= 0 and k!= 0:
		dp[0][j][k] = dp[0][j-1][k-1] + arr_y[j-1]*arr_z[k-1]
			
for i in range(1,x):
	for k in range(1,z):
		# if i!= 0 and k!= 0:
		dp[i][0][k] = dp[i-1][0][k-1] + arr_x[i-1]*arr_z[k-1]

for i in range(1, x):
	for j in range(1, y):
		for k in range(1, z):
			opt1 = dp[i-1][j-1][k] + arr_x[i-1]*arr_y[j-1]
			opt2 = dp[i][j-1][k-1] + arr_y[j-1]*arr_z[k-1]
			opt3 = dp[i-1][j][k-1] + arr_x[i-1]*arr_z[k-1]
			# opt2 = d
			dp[i][j][k] = max(opt1, opt2, opt3)

ans = dp[x-1][y-1][z-1]
# used_x = 0
# used_y = 0
# used_z = 0
# used = [used_x, used_y, used_z]
# while(True):
# 	poss = []
# 	for i in range(3):
# 		if used[i] < lengths[i]:
# 			poss.append((arrs[i][used[i]], i))

# 	if len(poss) <= 1:
# 		break

# 	else:
# 		poss.sort()
# 		v1, t1 = poss[-1]
# 		v2, t2 = poss[-2]

# 		ans += v1*v2
# 		used[t1] += 1
# 		used[t2] += 1

print(ans)	
# answers.append(ans)

# print(*answers, sep = '\n')
