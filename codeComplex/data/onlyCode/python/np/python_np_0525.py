import sys;input = sys.stdin.readline;n, k = map(int, input().split());s = input()[:-1];left, right = 0, n
while left < right:
    mid = right - (right - left) // 2;A = [[0] * (n + 2) for _ in range(k)]
    for c in range(k):
        A[c][n] = A[c][n + 1] = n + 1;L = 0
        for i in range(n - 1, -1, -1):L = (L + 1 if s[i] == '?' or ord(s[i]) - ord('a') == c else 0);A[c][i] = i + mid if L >= mid else A[c][i + 1]
    dp = [n + 1] * (1 << k);dp[0] = 0
    for mask in range(1 << k):
        for i in range(k):
            if mask >> k & 1: continue
            t = mask | 1 << i;dp[t] = min(dp[t], A[i][dp[mask]])
    if dp[-1] <= n: left = mid
    else: right = mid - 1
print(left)