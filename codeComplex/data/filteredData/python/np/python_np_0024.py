import random

maxbits = 22
maxmask = 1 << maxbits

def main(n: int):
    # 1. 生成测试数据：n 个随机整数，范围 [0, maxmask-1]
    # 如需固定数据，可改为手动构造 a
    a = [random.randint(0, maxmask - 1) for _ in range(n)]

    # 2. 原逻辑开始
    dp = [-1] * maxmask

    for x in a:
        dp[x] = x

    for exp in range(maxbits):
        bit = 1 << exp
        for i in range(maxmask):
            if i & bit:
                if dp[i] == -1:
                    dp[i] = dp[i - bit]

    res = []
    full = maxmask - 1
    for i in range(n):
        res.append(str(dp[full ^ a[i]]))

    # 输出结果
    print(" ".join(res))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)