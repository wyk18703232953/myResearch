def main(n):
    # 生成测试数据：将原来的 k 设为和 n 同规模，例如 k = n // 2（可按需调整）
    k = max(1, n // 2)

    x, y = 1, n
    f = 0
    m = 0  # 为了在循环后可用

    while x <= y:
        m = (x + y) // 2

        # 计算 m 的数位和
        s = 0
        p = m
        while p > 0:
            s += p % 10
            p //= 10

        # 计算 m-1 的数位和
        m1 = m - 1
        s1 = 0
        p = m1
        while p > 0:
            s1 += p % 10
            p //= 10

        if m == 0 or (m - s >= k and m1 - s1 < k):
            f = 1
            break
        elif m - s < k:
            x = m + 1
        else:
            y = m - 1

    if f:
        print(n - m + 1)
    else:
        print(0)


if __name__ == "__main__":
    # 示例：运行 main，指定规模 n
    main(10**6)