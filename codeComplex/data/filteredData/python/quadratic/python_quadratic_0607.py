def main(n):
    """
    n: 数据规模，用于生成测试数据
    """
    import random

    # 根据 n 生成 N, M, K
    # 这里约定：
    #   N = n
    #   1 <= M <= N
    #   K 为 1 到 10 之间的整数
    N = max(1, n)
    M = random.randint(1, N)
    K = random.randint(1, 10)

    # 生成长度为 N 的数组 arr，元素范围可根据需求调整
    # 这里用 -10 到 10 之间的随机整数
    arr = [random.randint(-10, 10) for _ in range(N)]

    res = 0
    for j in range(M):
        s = 0
        mini = 0
        for i in range(j, N):
            if i % M == j:
                mini = min(mini, s)
                s -= K
            s += arr[i]
            res = max(res, s - mini)

    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的测试数据并运行逻辑
    main(10)