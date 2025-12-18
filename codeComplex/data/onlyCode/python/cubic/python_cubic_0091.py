def func():
    N = 520
    K = 12
    C = 100 * 1000 + 11
    n, k = [int(x) for x in list(raw_input().split(' '))]
    c = [0 for _ in range(C)]
    f = [0 for _ in range(C)]

    dp = [[0 for _ in range(K*(N))] for _ in range(N)]

    a = [int(x) for x in list(raw_input().split(' '))]
    for x in a:
        c[x] += 1

    b = [int(x) for x in list(raw_input().split(' '))]
    for x in b:
        f[x] += 1

    h = [0]+[int(x) for x in list(raw_input().split(' '))]

    for i in range(n):
        for j in range(n*k + 1):
            for cur in range(k+1):
                dp[i + 1][j + cur] = max(dp[i + 1][j + cur], dp[i][j] + h[cur])

    ans = 0
    for i in range(C):
        if f[i] != 0:
            ans += dp[f[i]][c[i]]

    return ans


if __name__ == "__main__":
    print(func())
