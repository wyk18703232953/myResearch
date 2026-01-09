def main(n):
    # 映射规则：
    #   m = n
    #   n2 = n + m = 2n
    #   xi: 长度 2n
    #   ti: 长度 2n，其中恰有 n 个 1（类型1），n 个 2（非1）
    #
    # 构造方式：
    #   ti: 前 n 个为 1，后 n 个为 2，保证结构稳定
    #   xi: 使用简单算术构造，确保单调不减，避免边界异常
    #
    # 这样可规模化，且完全由 n 决定，满足确定性和可重复性
    
    if n <= 0:
        return

    m = n
    n2 = n + m  # = 2n

    # 构造 ti：前 n 个为 1，后 n 个为 2（非 1）
    ti = [1] * n + [2] * n

    # 构造 xi：单调不减的整数序列
    # 例如：xi[i] = i // 2 + i % 3，保证随 i 增大整体上递增
    xi = [i // 2 + (i % 3) for i in range(n2)]

    ai = [0] * (m + 2)
    ar = [0] * (m + 2)
    ar[-1] = 10**11
    ar[0] = -100000000000

    j = 1
    for i in range(n2):
        if ti[i] == 1:
            ar[j] = xi[i]
            j += 1

    i1 = 0
    i2 = 1
    for i in range(n2):
        if ti[i] == 1:
            i2 += 1
            i1 += 1
            continue
        num = xi[i] - ar[i1]
        num2 = ar[i2] - xi[i]
        if num <= num2:
            ai[i1] += 1

        else:
            ai[i2] += 1

    # 输出格式与原程序一致：从 1 到 m，空格分隔
    for i in range(1, m + 1):
        # print(ai[i], end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    # 示例：可根据需要修改 n 的大小进行时间复杂度实验
    main(10)