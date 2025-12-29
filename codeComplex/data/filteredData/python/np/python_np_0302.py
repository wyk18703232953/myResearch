def main(n: int):
    # n 为规模，这里我们自行生成 K
    # 示例：令 K = n // 2（至少为 1，至多为 n）
    K = max(1, min(n, n // 2 if n >= 2 else 1))

    mod = 998244353
    if K == 1:
        print(2)
        return

    dp = [[0] * 4 for _ in range(K + 1)]
    dp[1][0] = 1
    if K >= 2:
        dp[2][1] = 1
        dp[2][2] = 1
    dp[1][3] = 1

    for _ in range(1, n):
        nx = [[0] * 4 for _ in range(K + 1)]
        for k in range(K + 1):
            for j in range(4):
                val = dp[k][j] % mod
                if val == 0:
                    continue
                if j == 0:
                    nx[k][0] = (nx[k][0] + val) % mod
                    if k + 1 <= K:
                        nx[k + 1][1] = (nx[k + 1][1] + val) % mod
                        nx[k + 1][2] = (nx[k + 1][2] + val) % mod
                        nx[k + 1][3] = (nx[k + 1][3] + val) % mod
                elif j == 1:
                    nx[k][0] = (nx[k][0] + val) % mod
                    nx[k][1] = (nx[k][1] + val) % mod
                    if k + 2 <= K:
                        nx[k + 2][2] = (nx[k + 2][2] + val) % mod
                    nx[k][3] = (nx[k][3] + val) % mod
                elif j == 2:
                    nx[k][0] = (nx[k][0] + val) % mod
                    if k + 2 <= K:
                        nx[k + 2][1] = (nx[k + 2][1] + val) % mod
                    nx[k][2] = (nx[k][2] + val) % mod
                    nx[k][3] = (nx[k][3] + val) % mod
                else:
                    if k + 1 <= K:
                        nx[k + 1][0] = (nx[k + 1][0] + val) % mod
                        nx[k + 1][1] = (nx[k + 1][1] + val) % mod
                        nx[k + 1][2] = (nx[k + 1][2] + val) % mod
                    nx[k][3] = (nx[k][3] + val) % mod
        dp = nx

    print(sum(dp[K]) % mod)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)