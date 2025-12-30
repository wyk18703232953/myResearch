import math
import random

def max_sub(arr, n):
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(0, max(dp))


def solve(n, m, k, arr):
    q = -math.inf
    # dp[i][j]: at position i, remainder j (mod m)
    dp = [[q] * (m + 1) for _ in range(n)]

    if m == 1:
        for i in range(n):
            arr[i] = arr[i] - k
        return max_sub(arr, n)
    else:
        for i in range(n):
            dp[i][1] = arr[i] - k
            for j in range(1, m + 1):
                if i - 1 < 0 or dp[i - 1][j] == q:
                    continue
                nxt = (j + 1) % m
                if nxt == 0:
                    nxt = m
                if nxt != 1:
                    dp[i][nxt] = max(dp[i][nxt], dp[i - 1][j] + arr[i])
                else:
                    dp[i][nxt] = max(dp[i][nxt], arr[i] - k, dp[i - 1][j] + arr[i] - k)

        ma = 0
        for i in range(n):
            for j in range(1, m + 1):
                ma = max(ma, dp[i][j])
        return ma


def main(n):
    # 生成测试数据：
    # n: 数组长度（由调用者指定）
    # m: 1 到 min(10, n) 之间
    # k: 1 到 10 之间
    # arr: 元素在 [-10, 10] 之间
    if n <= 0:
        return 0

    random.seed(0)
    m = random.randint(1, min(10, n))
    k = random.randint(1, 10)
    arr = [random.randint(-10, 10) for _ in range(n)]

    ans = solve(n, m, k, arr)
    print(ans)
    return ans