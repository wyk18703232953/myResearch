def main(n):
    N = 520
    K = 12
    C = 100 * 1000 + 11

    # 映射 n 到原程序的 n,k
    # n1: 原程序中的 n，控制 dp 的行数
    # k1: 原程序中的 k，控制 dp 的列扩展
    n1 = max(1, min(n, N - 1))
    k1 = max(1, min(n % (K + 1), K))
    n_input = n1
    k_input = k1

    c = [0 for _ in range(C)]
    f = [0 for _ in range(C)]
    dp = [[0 for _ in range(K * (N))] for _ in range(N)]

    # 生成 a，长度为 n_input，元素在 [0, C-1]
    a = [(i * 7 + 3) % C for i in range(n_input)]
    for x in a:
        c[x] += 1

    # 生成 b，长度为 n_input，元素在 [0, C-1]
    b = [(i * 13 + 5) % C for i in range(n_input)]
    for x in b:
        f[x] += 1

    # 生成 h，长度为 k_input+1，h[0] = 0
    h = [0] + [((i * 5 + 1) // 2) for i in range(1, k_input + 1)]

    for i in range(n_input):
        for j in range(n_input * k_input + 1):
            for cur in range(k_input + 1):
                dp[i + 1][j + cur] = max(dp[i + 1][j + cur], dp[i][j] + h[cur])

    ans = 0
    for i in range(C):
        if f[i] != 0:
            ans += dp[f[i]][c[i]]

    return ans


if __name__ == "__main__":
    # print(main(10))
    pass