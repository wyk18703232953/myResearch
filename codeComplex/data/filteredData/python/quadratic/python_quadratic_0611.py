import sys
import math
import queue
import random

MOD = 998244353
sys.setrecursionlimit(1000000)


def solve(n, m, k, a):
    dp = [[-10 ** 20 for _ in range(m)] for _ in range(n)]
    dp[0][0] = a[0] - k

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = max(dp[i - 1][m - 1] + a[i], a[i]) - k
            else:
                dp[i][j] = dp[i - 1][j - 1] + a[i]

    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    return ans


def main(n):
    # 根据规模 n 生成测试数据：
    # 让 m 和 k 为 n 的简单函数，并生成一个长度为 n 的数组 a
    if n <= 0:
        return

    m = max(1, n // 3 + 1)          # 1 <= m <= n，大致和 n 同阶但更小
    k = max(1, n // 5 + 1)          # 正整数 k，随 n 变化
    # 随机生成 a，取值范围随 n 线性增长，既有正有负
    random.seed(0)
    a = [random.randint(-n, n) for _ in range(n)]

    ans = solve(n, m, k, a)
    print(ans)


if __name__ == "__main__":
    # 示例调用，可以按需修改 n
    main(10)