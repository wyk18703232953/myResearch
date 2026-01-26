from collections import defaultdict
from math import gcd

def main(n):
    # Generate deterministic input based on n
    # Interpret n as the length of A and B
    if n <= 0:
        print(-1)
        return

    A = [i + 1 for i in range(n)]
    B = [(i * 2 + 1) for i in range(n)]

    dp = defaultdict(lambda: float("inf"))
    for a, b in zip(A, B):
        dp[a] = min(dp[a], b)
        for d in list(dp.keys()):
            cur = gcd(a, d)
            dp[cur] = min(dp[cur], dp[a] + dp[d])
    if 1 not in dp:
        print(-1)
    else:
        print(dp[1])

if __name__ == "__main__":
    main(10)