from collections import defaultdict
from math import gcd
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = defaultdict(lambda: float("inf"))
for a, b in zip(A, B):
    dp[a] = min(dp[a], b)
    for d in dp.copy():
        cur = gcd(a, d)
        dp[cur] = min(dp[cur], dp[a] + dp[d])
if 1 not in dp:
    print(-1)
else:
    print(dp[1])