def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里假设：
    - M = 10 * n
    - N = n
    - 在 [1, M-1] 范围内生成严格递增的 N 个灯位置
    """
    import random

    if n <= 0:
        return

    M = 10 * n
    N = n

    # 生成 N 个严格递增的灯位置
    # 为简单起见，先生成候选集合再选取并排序
    positions = sorted(random.sample(range(1, M), N))

    light = [0] + positions + [M]
    sumlist = []
    sumlight = 0
    ans = -10**30

    for i in range(N + 1):
        sumlight += (-1) ** (i + 1) * light[i]
        sumlist.append(sumlight)

    for i in range(1, N + 1):
        if light[i] > light[i - 1] + 1:
            ans = max(
                ans,
                2 * sumlist[i - 1] - sumlight + (-1) ** (i + 1) * (light[i] - 1),
            )
        if light[i] < light[i + 1] - 1:
            ans = max(
                ans,
                2 * sumlist[i] - sumlight + (-1) ** i * (light[i] + 1),
            )

    if N % 2 == 0:
        result = max(ans, sumlight + M)
    else:
        result = max(ans + M, sumlight)

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)