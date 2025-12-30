from collections import defaultdict
import random

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据 X
    # 这里示例：X 为长度 n 的随机小整数序列
    # 如需特定分布，可在此修改
    random.seed(0)
    X = [random.randint(0, 3) for _ in range(n)]

    # 2. 原逻辑实现
    dp = defaultdict(lambda: -1)
    M = 1000

    # 初始化 dp，对于长度为 1 的区间
    for i in range(n):
        dp[i + M] = X[i]

    # 枚举区间长度 i
    for i in range(2, n + 1):
        # 枚举区间起点 j
        for j in range(n - i + 1):
            # 枚举切分点 k
            for k in range(1, i):
                u = dp[j + M * k]
                v = dp[j + k + M * (i - k)]
                if u == -1 or v == -1 or u != v:
                    continue
                dp[j + M * i] = u + 1
                break

    dp2 = [0] * (n + 1)
    for i in range(n):
        dp2[i + 1] = dp2[i] + 1
        for j in range(i + 1):
            if dp[j + (i + 1 - j) * M] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    # 输出与原程序一致（返回最终答案）
    print(dp2[-1])
    return dp2[-1]


if __name__ == "__main__":
    # 示例运行：规模 n = 10
    main(10)