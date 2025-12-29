import random

def main(n):
    # 生成测试数据
    # 随机生成数组 a，元素范围可按需调整
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 预处理 dp
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]

    count = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            dp[j][j + count] = dp[j][j + count - 1] ^ dp[j + 1][j + count]
        count += 1

    count = 1
    for i in range(n - 1):
        for j in range(n - i - 1):
            dp[j][j + count] = max(
                dp[j][j + count],
                dp[j][j + count - 1],
                dp[j + 1][j + count]
            )
        count += 1

    # 生成查询次数 q，并随机生成区间查询
    q = n  # 这里简单设为 n 次查询，可按需调整
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 输出查询结果
    for l, r in queries:
        l -= 1
        r -= 1
        print(dp[l][r])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)