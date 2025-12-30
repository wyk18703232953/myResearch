from itertools import accumulate
import random

def main(n):
    # 生成测试数据
    # n: 数组长度
    # k: 1 ~ n 之间的随机整数
    k = random.randint(1, n)
    a = [random.randint(-10, 10) for _ in range(n)]
    b = [random.randint(-10, 10) for _ in range(n)]

    # 原逻辑
    ps = list(accumulate(a))
    dp = [[0 for _ in range(2)] for _ in range(1 + n)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + a[i - 1] * b[i - 1]
        dp[i][1] = max(
            dp[i - 1][1] + a[i - 1] * b[i - 1],
            ps[i - 1] - (ps[i - k - 1] if i - k - 1 >= 0 else 0) + dp[max(i - k, 0)][0]
        )
    print(max(max(v) for v in dp))


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)