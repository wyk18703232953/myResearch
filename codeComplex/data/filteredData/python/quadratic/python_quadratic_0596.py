def main(n):
    # 映射含义：
    # m = n（循环周期）
    # 序列长度 len(a) = 3 * n
    # k = n // 2 + 1（保证随 n 变化）
    if n <= 0:
        return 0

    m = n
    k = n // 2 + 1
    a_len = 3 * n

    # 确定性构造 a
    # a[i] 在 [-k, k] 内波动
    a = [((i * 2) % (2 * k + 1)) - k for i in range(a_len)]

    def f(o):
        r = 0
        e = 0
        for i, x in enumerate(a):
            if i < o:
                continue
            if i % m == o:
                e -= k
                if e < -k:
                    e = -k
            e += x
            if e > r:
                r = e
        return r

    ans = max(f(o) for o in range(m))
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例：选择一个规模 n 调用
    main(10)