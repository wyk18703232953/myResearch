def main(n):
    # 依据规模 n 构造一组 (n, k)
    # 保证 1 <= k <= n
    k = n // 2 + 1

    # 原逻辑开始
    i = 0
    t = 0
    while k > i:
        t += 1
        i += t
    c = n - t
    i -= c
    while i != k:
        t += 1
        i += t + 1
        c -= 1
    print(c)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)