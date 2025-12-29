import random

def main(n):
    # 生成测试数组 a（1 <= a[i] <= 10^9）
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 预处理 dp
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i + 1):
            dp[i][j] = dp[i - 1][j] ^ dp[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j + 1])

    # 生成查询次数 q 和查询区间 [l, r]
    q = max(1, n // 2)  # 示例：q 与 n 同级别
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 输出示例：先输出 a，再输出查询及答案
    print("n =", n)
    print("a =", a)
    print("q =", q)
    for l, r in queries:
        ans = dp[r - l][l - 1]
        print(f"query ({l}, {r}) -> {ans}")


if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)