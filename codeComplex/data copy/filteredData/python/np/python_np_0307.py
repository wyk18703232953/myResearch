import math
import copy
import collections
from collections import deque
import heapq
import itertools
from collections import defaultdict
from collections import Counter

mod = 998244353

def run_algorithm(n, k):
    dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
    dp[0][1][0] = 1
    if k >= 2:
        dp[0][2][1] = 1
    for i in range(1, n):
        for j in range(1, k + 1):
            dp[i][j][0] += dp[i - 1][j - 1][0] + dp[i - 1][j][0] + 2 * dp[i - 1][j][1]
            dp[i][j][0] %= mod
            if j - 2 >= 0:
                dp[i][j][1] += 2 * dp[i - 1][j - 1][0] + dp[i - 1][j][1] + dp[i - 1][j - 2][1]
            else:
                dp[i][j][1] += dp[i - 1][j - 1][0] + dp[i - 1][j][1] + dp[i][j - 1][0]
            dp[i][j][1] %= mod
    ans = 0
    for z in range(2):
        ans += dp[n - 1][k][z]
    ans *= 2
    return ans % mod

def main(n):
    if n < 2:
        n_internal = 2
    else:
        n_internal = n
    k = max(1, n_internal // 2)
    result = run_algorithm(n_internal, k)
    print(result)

if __name__ == "__main__":
    main(10)