def main(n):
    # 固定长度为 14，因为核心算法写死了 n = 14
    size = 14
    # 使用 n 生成一个确定性的长度为 14 的整数列表 b
    # 模式：b[i] = (i + 1) * (n % 10 + 1)
    base = n % 10 + 1
    b = [(i + 1) * base for i in range(size)]

    ans = 0
    for i in range(size):
        a = b.copy()
        if a[i] == 0:
            continue
        x = a[i]
        a[i] = 0
        full = x // size
        xex = x % size
        for j in range(size):
            a[j] += full
        for j in range(xex):
            a[(i + j + 1) % size] += 1
        pot = 0
        for j in a:
            if j % 2 == 0:
                pot += j
        ans = max(ans, pot)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：用若干不同规模调用 main
    main(1)
    main(10)
    main(100)