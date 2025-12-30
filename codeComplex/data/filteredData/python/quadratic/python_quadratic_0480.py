def main(n):
    """
    根据给定规模 n 生成一组满足条件的 L、R、C，并执行原逻辑。
    若生成失败（极小概率），会抛出异常。
    """

    import random

    # 为了可复现，可以固定随机种子；如不需要可注释掉
    random.seed(0)

    # 随机生成一个满足题意的 C（均为正整数）
    # 数值范围可以按需调整
    C = [random.randint(1, 10) for _ in range(n)]

    # 由 C 反推 L、R（按题意的定义：比 C[i] 大的数量）
    L = [0] * n
    R = [0] * n
    for i in range(n):
        ci = C[i]
        # 统计左侧比 C[i] 大的数量
        l = 0
        for j in range(i - 1, -1, -1):
            if C[j] > ci:
                l += 1
        # 统计右侧比 C[i] 大的数量
        r = 0
        for j in range(i + 1, n):
            if C[j] > ci:
                r += 1
        L[i] = l
        R[i] = r

    # 以下为原逻辑：给定 N, L, R，检查是否存在合法 C 并输出
    N = n

    C_check = [N - L[i] - R[i] for i in range(0, N)]

    for i, _ in enumerate(C_check):
        if C_check[i] <= 0:
            print("NO")
            return

        l = 0
        r = 0

        j = i - 1
        while j >= 0:
            if C_check[j] > C_check[i]:
                l += 1
            j -= 1

        j = i + 1
        while j < N:
            if C_check[j] > C_check[i]:
                r += 1
            j += 1

        if L[i] != l or R[i] != r:
            print("NO")
            return

    print("YES")
    for i in range(0, N - 1):
        print(C_check[i], end=" ")
    print(C_check[N - 1])


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)