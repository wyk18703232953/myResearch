def main(n):
    # n 作为数组长度
    N = max(1, n)

    # 确定性生成 A：简单循环模式
    A = [(i % 3) + 1 for i in range(N)]

    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    for l in range(N):
        dp[l][l + 1] = A[l]

    for d in range(2, N + 1):
        for l in range(N - d + 1):
            for t in range(1, d):
                if dp[l][l + t] == dp[l + t][l + d] and dp[l][l + t] != -1:
                    dp[l][l + d] = dp[l][l + t] + 1
                    break

    dp2 = [i for i in range(N + 1)]
    for r in range(1, N + 1):
        if dp[0][r] != -1:
            dp2[r] = 1
    for l in range(N):
        for r in range(l + 2, N + 1):
            if dp[l + 1][r] != -1:
                dp2[r] = min(dp2[l + 1] + 1, dp2[r])

            else:
                dp2[r] = min(dp2[l + 1] + (r - l - 1), dp2[r])

    return dp2[N]


if __name__ == "__main__":
    # 示例：对若干规模调用 main
    for n in [1, 2, 5, 10]:
        # print(n, main(n))
        pass