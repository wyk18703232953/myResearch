def main(n):
    # 解释规模映射：
    # x: 列表长度
    # y: 目标值，随 n 线性增长
    # z: 初始值，固定为 1
    # l: 确定性生成的整数序列，长度为 x=n

    if n <= 0:
        print(-1)
        return

    x = n
    y = 2 * n + 3
    z = 1
    l = [(i * 3 + 1) % (2 * n + 5) + 1 for i in range(x)]

    l.sort()
    c = 0
    s = z
    while s < y and c < x:
        c += 1
        s = s + l[x - c] - 1
    if s < y:
        print(-1)
    else:
        print(c)


if __name__ == "__main__":
    main(10)