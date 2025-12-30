import random

def main(n):
    # 生成测试数据
    # 数组 a，长度 n，元素为 0~10^9 的随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]
    # 生成若干随机查询，q 取 n，区间 [l, r] 满足 1 <= l <= r <= n
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 原始逻辑
    f = [[0] * n for _ in range(n)]
    for i in range(n):
        f[0][i] = a[i]
    for i in range(1, n):
        for j in range(n - i):
            f[i][j] = f[i - 1][j] ^ f[i - 1][j + 1]
    for i in range(1, n):
        for j in range(n - i):
            f[i][j] = max(f[i][j], f[i - 1][j], f[i - 1][j + 1])

    # 输出查询结果
    for l, r in queries:
        print(f[r - l][l - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)