import random

def main(n: int):
    # 生成测试数据：长度为 n 的随机整数数组 s，以及随机查询 q, (l, r)
    random.seed(0)
    s = [random.randint(0, 1000) for _ in range(n)]

    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # 初始化 dp 的第 0 层
    for i in range(n):
        dp[0][i] = s[i]

    # 先按原逻辑计算异或值
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]

    # 再按原逻辑做区间最大值的传递
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1], dp[i][j])

    # 生成查询个数 q 和 q 组随机查询 (l, r)，1 <= l <= r <= n
    q = max(1, n // 2)
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 按原程序逻辑输出结果
    for (l, r) in queries:
        print(dp[r - l][l - 1])


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)