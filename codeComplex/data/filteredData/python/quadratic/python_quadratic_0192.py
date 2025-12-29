import random

def main(n: int):
    # 生成长度为 n 的测试数组 l，取值范围可自行调整
    l = [random.randint(0, 10**9) for _ in range(n)]

    # 预处理 dp
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[0][i] = l[i]

    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]

    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # 生成测试查询数据 q 及若干随机区间查询
    q = n  # 例如生成 n 个查询
    queries = []
    for _ in range(q):
        x = random.randint(1, n)
        y = random.randint(x, n)  # 保证 x <= y
        queries.append((x, y))

    # 执行查询并输出结果
    for x, y in queries:
        x -= 1
        y -= 1
        print(dp[y - x][x])


if __name__ == "__main__":
    # 可以在此处修改 n 的默认测试规模
    main(5)