import sys
import math
import queue
import random

MOD = 998244353
sys.setrecursionlimit(1000000)


def main(n: int):
    # 生成规模为 n 的测试数据
    # 为了更贴近原题场景，这里随机生成 m、k 和数组 a
    #
    # 限制条件可以按需要调整：
    # 1 <= m <= n
    # k 在 [-10^4, 10^4] 范围内
    # a[i] 在 [-10^4, 10^4] 范围内
    if n <= 0:
        print(0)
        return

    random.seed(0)  # 固定种子，保证复现性
    m = random.randint(1, max(1, n))          # 1 <= m <= n
    k = random.randint(-10_000, 10_000)       # k 范围可按需求修改
    a = [random.randint(-10_000, 10_000) for _ in range(n)]

    # 动态规划主逻辑（与原程序等价）
    dp = [[-10 ** 20 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(min(m, i + 1)):
            if j == 0:
                # 由上一组的最后一个状态转移，或从当前元素单独开始
                dp[i][j] = max(dp[i - 1][m - 1] + a[i], a[i]) - k
            else:
                dp[i][j] = dp[i - 1][j - 1] + a[i]

    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    print(ans)


if __name__ == "__main__":
    # 示例：可在此处指定 n 进行简单测试
    main(5)