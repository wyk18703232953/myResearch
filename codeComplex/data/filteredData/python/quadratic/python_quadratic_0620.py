def main(n):
    # 映射含义：
    # n -> 数组长度 n
    # 令 m = max(1, n // 3)
    # 令 k = max(1, n // 5)
    if n <= 0:
        return 0

    m = max(1, n // 3)
    k = max(1, n // 5)

    # 确定性生成数组 a，长度为 n
    # 使用简单算术构造
    a = [(i * 7 + i // 3 - i % 5) for i in range(n)]

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
    return ret


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做时间复杂度实验
    main(10)