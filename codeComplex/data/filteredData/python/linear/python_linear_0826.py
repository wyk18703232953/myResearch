import math
import random

def main(n):
    # 生成测试数据：
    # 1. 随机生成查询次数 t
    # 2. 对每个查询：随机生成 k (1 <= k <= n)，随机生成长度为 n 的字符串 s（字符集为 'R','G','B'）
    t = random.randint(1, 5)  # 可调整查询次数范围
    rgb = 'RGB'

    for _ in range(t):
        k = random.randint(1, n)
        s = ''.join(random.choice(rgb) for _ in range(n))

        # 以下为原逻辑
        ans = math.inf
        for start in range(3):
            dp = [0] * (n + 1)
            for i in range(n):
                cur = rgb[(start + i) % 3]
                dp[i + 1] = dp[i] + (s[i] != cur)
            for i in range(n - k + 1):
                ans = min(ans, dp[i + k] - dp[i])
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，规模为 n=10
    main(10)