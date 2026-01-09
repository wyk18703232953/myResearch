def main(n):
    # 映射规则：
    # n >= 2
    # m = max(1, n // 3)
    # k = max(1, n // 5)
    if n < 2:
        n = 2
    m = max(1, n // 3)
    k = max(1, n // 5)

    # 确定性生成 a，长度为 n
    # a[j] = (j % 7) - 3 => 值域在 [-3, 3]
    a = [(j % 7) - 3 for j in range(n)]

    ret = 0
    for i in range(m):
        cur = 0
        for j in range(i, n):
            if j % m == i:
                cur = max(0, cur)
                cur -= k
            cur += a[j]
            ret = max(ret, cur)
    # print(ret)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 100 作为输入规模
    main(100)