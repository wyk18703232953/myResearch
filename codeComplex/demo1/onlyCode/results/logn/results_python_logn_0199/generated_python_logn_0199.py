def main(n):
    # 生成测试数据：N = n，S 取一个相对中间的值，例如 N 的一半
    N = n
    S = max(0, N // 2)

    def BIG(NUM):
        X = NUM
        SM = 0
        while X != 0:
            M = X % 10
            SM += M
            X //= 10
        return NUM - SM >= S

    F = 0
    L = N + 1
    MN = 1 << 64

    while L >= F:
        M = (L + F) >> 1
        if BIG(M):
            L = M - 1
            if M < MN:
                MN = M
        else:
            F = M + 1

    if MN == 1 << 64:
        print(0)
    else:
        print(N - MN + 1)


if __name__ == "__main__":
    # 示例：可以在此处修改 n 的值进行测试
    main(1000000)