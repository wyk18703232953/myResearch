import sys

#comment these out later
#sys.stdin = open("in.in", "r")
#sys.stdout = open("out.out", "w")

#WLOG i, n = x, j, m = y

inp = [int(x) for x in sys.stdin.read().split()]; ii = 0

n = inp[ii]; ii += 1
m = inp[ii]; ii += 1
k = inp[ii]; ii += 1

if k%2 == 1:
	for _ in range(n):
		toprint = ["-1" for __ in range(m)]
		print(" ".join(toprint))

	sys.exit()


yw = []

for _ in range(n):
	yw.append(inp[ii:ii+m-1])
	ii += m-1


xw = []

for _ in range(n-1):
	xw.append(inp[ii:ii+m])
	ii += m

inf = 10**10

#dp[i][j]

steps = k//2

dp = [[[inf for _ in range(m)] for _ in range(n)] for _ in range(steps+1)]

for i in range(n):
	for j in range(m):
		dp[0][i][j] = 0

#dp[i][j] = min of (1) dp[i][j] (2) dp[i-1][j] + w (3) dp[i][j-1] + w 
#(4) dp[i+1][j] + w (5) dp[i][j+1] + w

for step in range(1, steps + 1):
	for i in range(n):
		for j in range(m):
			#i, j go 1-n, 1-m

			if i > 0:
				dp[step][i][j] = min(dp[step][i][j], dp[step-1][i-1][j] + xw[i-1][j])

			if i < n-1:
				dp[step][i][j] = min(dp[step][i][j], dp[step-1][i+1][j] + xw[i][j])

			if j > 0:
				dp[step][i][j] = min(dp[step][i][j], dp[step-1][i][j-1] + yw[i][j-1])

			if j < m-1:
				dp[step][i][j] = min(dp[step][i][j], dp[step-1][i][j+1] + yw[i][j])

for x in dp[-1]:
	print(" ".join(list(map(str, [2*o for o in x]))))