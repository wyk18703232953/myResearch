def main(n):
    # 确定性生成 n, m, k 和数组 A
    # n 为主规模，m、k 和 A 都由固定规则从 n 推导，保证可重复、可规模化
    if n <= 0:
        return 0

    m = max(1, n // 2)
    k = n // 3

    # 构造长度为 n 的数组 A
    # 使用简单算术构造，完全确定性
    A = [(i * 7 + n) % (n + 5) for i in range(n)]

    if n <= m:
        AA = [0] * (n + 1)
        for i in range(n):
            AA[i + 1] = AA[i] + A[i]
        mm = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                mm = max(mm, AA[j] - AA[i] - k)
        result = max(A[0] - k, 0) if n == 1 else mm

    else:
        DP = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            a = A[i]
            DP[i + 1][0] = max(DP[i][0], DP[i][m], DP[i][m] + a - k, DP[i][1])
            DP[i + 1][1] = max(a - k, DP[i][m] + a - k)
            for j in range(2, m + 1):
                DP[i + 1][0] = max(DP[i + 1][0], DP[i][j])
                if j > i + 1:
                    continue

                else:
                    DP[i + 1][j] = max(DP[i][j - 1] + a, DP[i][m] + a - k)
        result = max(0, max(DP[n]))
    return result


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n，用于不同规模的时间复杂度实验
    for test_n in [1, 5, 10, 50, 100]:
        # print(test_n, main(test_n))
        pass