def main(n):
    # 映射含义：
    # n: 序列长度，同时也作为原程序的 n
    # m, k 由 n 确定性生成
    # 保持原算法逻辑不变

    if n <= 0:
        return 0

    # 确定性生成 m, k
    # 保证 1 <= m <= n（当 n >= 1）
    m = max(1, n // 2)
    k = n // 3 + 1

    # 确定性生成数组 A，长度为 n
    # 元素既有增长又有周期变化，避免全相同
    A = [(i * 7 + i % 5 - i // 3) for i in range(1, n + 1)]

    if n <= m:
        AA = [0] * (n + 1)
        for i in range(n):
            AA[i + 1] = AA[i] + A[i]
        mm = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                mm = max(mm, AA[j] - AA[i] - k)
        ans = max(A[0] - k, 0) if n == 1 else mm

    else:
        DP = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            a = A[i]
            DP[i + 1][0] = max([DP[i][0], DP[i][m], DP[i][m] + a - k, DP[i][1]])
            DP[i + 1][1] = max(a - k, DP[i][m] + a - k)
            for j in range(2, m + 1):
                DP[i + 1][0] = max(DP[i + 1][0], DP[i][j])
                if j > i + 1:
                    continue

                else:
                    DP[i + 1][j] = max(DP[i][j - 1] + a, DP[i][m] + a - k)
        ans = max(0, max(DP[n]))

    return ans


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的规模做时间复杂度实验
    for n in [10, 100, 1000]:
        # print(n, main(n))
        pass