def main(n):
    # 映射：给定 n，构造 m、k 和长度为 n 的数组 a
    # 这里令 m = max(1, n // 3)，k = max(1, n // 5)
    if n <= 0:
        print(0)
        return

    m = max(1, n // 3)
    k = max(1, n // 5)

    # 确定性构造 a：使用简单算术和取模
    a = [((i * 7) % 20) - 10 for i in range(n)]

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
    # 示例调用：可根据需要修改 n
    main(10)