def main(n):
    """
    n: 规模，对应原代码中的 n
    本实现自动生成一个测试用的 k，并输出结果。
    由于原代码中 j 的上界与 N*2-5 有关，k 必须在 [0, 2*N-1] 范围内。
    这里简单取 k = min(2*n - 1, n) 作为测试数据。
    """
    m = 998244353
    # 为安全，构造 DP 时的 N 至少要 >= n，并稍微大一些避免边界问题
    N = max(n + 5, 10)

    # dp[i][j][state]，i: 步数(0..N-1)，j: 计数(0..2*N-1)，state: 0..3
    dp = [[[0] * 4 for _ in range(N * 2)] for _ in range(N)]

    # 初始条件与原代码相同
    dp[0][1][0] = 1
    dp[0][1][1] = 1
    dp[0][2][2] = 1
    dp[0][2][3] = 1

    for i in range(N - 1):
        for j in range(1, N * 2 - 5):
            for me in range(4):
                val = dp[i][j][me]
                if not val:
                    continue
                for he in range(4):
                    if me <= 1:
                        if he <= 1:
                            nj = j + (he != me)
                            dp[i + 1][nj][he] = (dp[i + 1][nj][he] + val) % m

                        else:
                            nj = j + 1
                            dp[i + 1][nj][he] = (dp[i + 1][nj][he] + val) % m

                    else:
                        if he <= 1:
                            nj = j
                            dp[i + 1][nj][he] = (dp[i + 1][nj][he] + val) % m

                        else:
                            nj = j + (he != me) * 2
                            dp[i + 1][nj][he] = (dp[i + 1][nj][he] + val) % m

    # 生成测试用 k
    k = min(2 * N - 1, n)

    # 输出对应 n-1 行、列 k 的四种状态之和
    if n - 1 < N and 0 <= k < 2 * N:
        # print(sum(dp[n - 1][k]) % m)
        pass

    else:
        # 若 n 或 k 超出预设 dp 范围则输出 0（或按需要调整）
        # print(0)
        pass
if __name__ == "__main__":
    # 示例：调用 main(5)，可自行修改测试规模
    main(5)