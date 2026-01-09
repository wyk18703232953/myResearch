def main(n):
    # 映射：n 为数组长度，p 为一个与 n 相关的确定性值
    if n <= 0:
        return 0

    p = n + 7  # 确定性构造的模数

    # 确定性生成数组 a，长度为 n
    a = [(i * 3 + 1) % (p + 5) for i in range(n)]

    t = 0
    k = 0
    for i in range(n):
        k += a[i]
    s = 0
    for i in range(0, n - 1):
        s += a[i]
        t = max(t, s % p + (k - s) % p)
    # print(t)
    pass
    return t


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小进行时间复杂度实验
    main(10)