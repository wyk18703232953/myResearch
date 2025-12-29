import random

def main(n: int):
    # 生成测试数据：规模为 n，生成一个合适的模数 M（质数）
    N = n
    # 简单选取一个大于 N 的固定质数作为模数
    # 若 N 很大可改为更大的质数
    M = 10**9 + 7

    fac = [1] + [0] * N
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % M

    fac_inv = [0] * N + [pow(fac[N], M - 2, M)]
    for i in range(N, 0, -1):
        fac_inv[i - 1] = fac_inv[i] * i % M

    pow2 = [1] + [0] * N
    for i in range(N):
        pow2[i + 1] = pow2[i] * 2 % M

    DP = [[0] * N for _ in range(N + 2)]
    DP[0][0] = 1
    for i in range(N):
        for j in range(N):
            DP[i][j] %= M
            if DP[i][j]:
                for k in range(i + 2, N + 2):
                    DP[k][j + 1] += (
                        DP[i][j]
                        * fac_inv[k - i - 1]
                        % M
                        * pow2[k - i - 2]
                        % M
                    )
    ans = 0
    for j in range(N):
        DP[N + 1][j] %= M
        if DP[N + 1][j]:
            ans += DP[N + 1][j] * fac[N - j + 1] % M
    ans %= M

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)