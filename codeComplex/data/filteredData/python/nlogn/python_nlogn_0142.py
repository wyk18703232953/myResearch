def main(n):
    # n 表示数组长度
    if n <= 0:
        print(0)
        return

    # 确定性生成 k 和数组 l
    # k 至少为 2，避免除以 0 或无意义情况
    k = (n % 7) + 2

    # 生成长度为 n 的数组 l，使用简单算术构造
    l = [(i * 3 + 1) % (5 * n + 7) for i in range(n)]
    l.sort()

    res = set()
    for i in l:
        if i % k != 0:
            res.add(i)
        elif i // k not in res:
            res.add(i)
    print(len(res))


if __name__ == "__main__":
    main(10)