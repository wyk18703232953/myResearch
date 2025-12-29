from collections import defaultdict
import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据 X
    # 这里示例生成范围在 [-5, 5] 的随机整数
    random.seed(0)
    X = [random.randint(-5, 5) for _ in range(n)]

    N = n
    dp = defaultdict(lambda: -1)

    # 初始化 dp
    for i in range(N):
        dp[i + 1001] = X[i]

    # 三重循环进行 dp 填充
    for i in range(2, N + 1):
        for j in range(N - i + 1):
            for k in range(1, i):
                u, v = dp[j + 1001 * k], dp[j + k + 1001 * (i - k)]
                if u == -1 or v == -1 or u != v:
                    continue
                dp[j + 1001 * i] = u + 1
                break

    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = dp2[i] + 1
        if dp[1001 * (i + 1)] != -1:
            dp2[i + 1] = 1
            continue
        for j in range(i + 1):
            if dp[j + (i + 1 - j) * 1001] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    print(dp2[-1])


if __name__ == "__main__":
    # 示例调用：规模 n=5
    main(5)