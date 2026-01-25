def main(n):
    # 映射：n -> 数组长度；m 和 k 由 n 确定性生成
    if n <= 0:
        print(0)
        return

    m = max(1, n // 3)
    k = max(1, n // 5)

    a = [(i * 2 - (n // 2)) for i in range(n)]

    ret = 0
    for i in range(m):
        cur = 0
        for j in range(i, n):
            if j % m == i:
                cur = max(0, cur)
                cur -= k
            cur += a[j]
            ret = max(ret, cur)
    print(ret)


if __name__ == "__main__":
    main(1000)