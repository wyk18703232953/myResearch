import random

def main(n: int):
    # 生成长度为 n 的随机数组 a，元素范围可根据需要调整
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 随机生成查询数量 q
    q = random.randint(1, max(1, n))

    # 每个查询生成一个合法区间 [l, r]，1 <= l <= r <= n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原始逻辑开始
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        dp[0][i] = a[i]

    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]

    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # 输出测试数据和结果，方便验证
    print("n =", n)
    print("a =", " ".join(map(str, a)))
    print("q =", q)
    print("queries:")
    for l, r in queries:
        print(l, r)
    print("answers:")
    for l, r in queries:
        print(dp[r - l][l - 1])


if __name__ == "__main__":
    # 示例：规模为 5，可根据需要修改或在外部调用 main(n)
    main(5)