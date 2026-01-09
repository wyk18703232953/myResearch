def main(n):
    # 为了保持原算法结构，需要 n, m, k, a
    # 将输入规模映射为 n；设 m 与 n 同阶，k 为常数
    if n <= 0:
        # print(0)
        pass
        return

    m = max(1, n // 3 + 1)
    k = 5

    # 构造长度为 n 的确定性整数数组 a
    # 示例：a[i] = (i % 7) - 3，包含正负和零
    a = [(i % 7) - 3 for i in range(n)]

    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + m * a[i - 1] - k

    M = [10 ** 20] * m
    ans = 0
    for i in range(0, n + 1):
        M[i % m] = min(M[i % m], b[i])
        for j in range(0, m):
            if i > j:
                ans = max(ans, b[i] - M[j] - k * ((m * i + m - (i - j)) % m))
    # print(ans // m)
    pass
if __name__ == "__main__":
    main(1000)