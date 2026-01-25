def main(n):
    # 映射 n 为 N 和 M，使规模随 n 线性增长
    # 这里固定 M = 2 * n，N = max(1, n)
    N = max(1, n)
    M = 2 * n if n > 0 else 2

    # 构造单调递增的 L[1..N]，范围在 [1, M-1]
    # 例如: L[i] = 1 + i * (M - 2) // (N + 1)
    # 保证 1 <= L[1] < ... < L[N] < M
    L_inner = [1 + i * (M - 2) // (N + 1) for i in range(1, N + 1)]
    L = [0] + L_inner + [M]

    sumL = [0]
    ans = -10**30
    for i in range(1, N + 1):
        sumL.append(sumL[-1] - (-1) ** i * L[i])
    for i in range(1, N + 1):
        if L[i] > L[i - 1] + 1:
            ans = max(ans, 2 * sumL[i - 1] - sumL[-1] - (-1) ** i * (L[i] - 1))
        if L[i] < L[i + 1] - 1:
            ans = max(ans, 2 * sumL[i] - sumL[-1] + (-1) ** i * (L[i] + 1))
    if N % 2 == 0:
        print(max(ans, sumL[-1] + M))
    else:
        print(max(ans + M, sumL[-1]))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)