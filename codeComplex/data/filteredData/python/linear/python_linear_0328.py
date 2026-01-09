def main(n):
    # 确定性数据生成：N=n，M=2*n，light 为严格递增位置
    N = n
    M = 2 * n
    # 生成一个递增序列，确保 1 <= light[0] < ... < light[N-1] < M
    # 例如：在区间 [1, M-1] 上均匀取 N 个点
    if N == 0:
        light = [0, M]

    else:
        light_positions = [(i + 1) * (M - 1) // (N + 1) for i in range(N)]
        # 保证严格递增且在 [1, M-1]
        for i in range(1, N):
            if light_positions[i] <= light_positions[i - 1]:
                light_positions[i] = light_positions[i - 1] + 1
        if light_positions[-1] >= M:
            light_positions[-1] = M - 1
        light = [0] + light_positions + [M]

    sumlist = []
    sumlight = 0
    ans = -10**30
    for i in range(N + 1):
        sumlight += (-1) ** (i + 1) * light[i]
        sumlist.append(sumlight)
    for i in range(1, N + 1):
        if light[i] > light[i - 1] + 1:
            ans = max(ans, 2 * sumlist[i - 1] - sumlight + (-1) ** (i + 1) * (light[i] - 1))
        if light[i] < light[i + 1] - 1:
            ans = max(ans, 2 * sumlist[i] - sumlight + (-1) ** i * (light[i] + 1))
    if N % 2 == 0:
        result = max(ans, sumlight + M)

    else:
        result = max(ans + M, sumlight)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)