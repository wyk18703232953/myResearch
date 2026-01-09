def BIG(NUM, S):
    X = NUM
    SM = 0
    while X != 0:
        M = X % 10
        SM += M
        X //= 10
    return NUM - SM >= S


def main(n):
    """
    n 为规模参数，用于生成 N 和 S 的测试数据。
    可根据需要修改测试数据生成方式。
    这里示例：
      N = n
      S = n // 2
    """
    N = n
    S = n // 2

    F = 0
    L = N + 1
    MN = 1 << 64

    while L >= F:
        M = (L + F) >> 1
        if BIG(M, S):
            L = M - 1
            if M < MN:
                MN = M

        else:
            F = M + 1

    if MN == 1 << 64:
        # print(0)
        pass

    else:
        # print(N - MN + 1)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(1000000)