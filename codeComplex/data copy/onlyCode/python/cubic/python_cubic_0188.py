n = int(input())
a = list(map(int, input().split(' ')))

new_a = [[0] * 600 for i in range(600)]
dp = [[0x7fffffff] * 600 for i in range(600)]

for i in range(n):
	new_a[i+1][i+1] = a[i]
	dp[i+1][i+1] = 1

for i in range(1, n + 1):
	for j in range(i + 1, n + 1):
		dp[i][j] = j - i + 1

for llen in range(2, n + 1):
	for left in range(1, n - llen + 2):
		right = left + llen - 1
		for middle in range(left, right):
			dp[left][right] = min(dp[left][right], dp[left][middle] + dp[middle+1][right])
			if dp[left][middle] == 1 and dp[middle+1][right] == 1 and new_a[left][middle] == new_a[middle+1][right]:
				dp[left][right] = 1
				new_a[left][right] = new_a[left][middle] + 1

print(dp[1][n])