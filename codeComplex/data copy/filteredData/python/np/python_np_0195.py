def main(n):
    # 为了保持与原程序输入结构一致：
    # 第一行: n, l, r, x
    # 第二行: n 个整数的列表 c
    # 将 n 作为题目中的 n，同时用确定性方式生成 l, r, x 和 c

    if n <= 0:
        print(0)
        return

    N = n
    # 确定性生成 l, r, x
    # 生成一个基础序列，用于构造 c 和边界
    c = [i * 3 + (i % 5) for i in range(N)]  # 单调递增，且跨度适中

    total_sum = sum(c)
    if total_sum == 0:
        l = 0
        r = 0
    else:
        # l 为总和的 1/3，r 为总和的 2/3，向下取整
        l = total_sum // 3
        r = (total_sum * 2) // 3

    # x 为元素范围跨度的一部分
    if N == 1:
        x = 0
    else:
        x = max(1, (c[-1] - c[0]) // 3)

    ways = 0
    for mask in range(0, 2 ** N):
        temp = 0
        m = 10 ** 9 + 1
        M = -1
        for j in range(0, N):
            if mask & (1 << j):
                temp += c[j]
                if c[j] < m:
                    m = c[j]
                if c[j] > M:
                    M = c[j]
        if m == 10 ** 9 + 1 and M == -1:
            continue
        if temp >= l and temp <= r and (M - m) >= x:
            ways += 1

    print(ways)


if __name__ == "__main__":
    main(10)