MOD = int(1e9 + 7)
N = 1030

def precompute_combinations():
    c = [[0] * N for _ in range(N)]
    for i in range(N):
        c[i][0] = 1
    for i in range(1, N):
        for j in range(1, N):
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD
    return c

def precompute_dp():
    dp = [0] * N
    for i in range(2, N):
        dp[i] = dp[bin(i).count('1')] + 1
    return dp

C = precompute_combinations()
DP = precompute_dp()

def solve(arr, cnt):
    if cnt == 0:
        return 1

    res = 0
    for i in range(1, N):
        if DP[i] != cnt - 1:
            continue
        n, k = len(arr) - 1, i
        for pos in range(len(arr)):
            if arr[pos] == 1:
                res = (res + C[n][k]) % MOD
                k -= 1
            n -= 1
        if n == -1 and k == 0:
            res = (res + 1) % MOD
    if cnt == 1:
        res = (res - 1) % MOD
    return res

def main(n):
    # 生成规模为 n 的测试数据
    # 这里生成一个长度为 n 的二进制数组和一个计数 cnt
    # 示例：交替 1 和 0，cnt 取 1..20 内的一个值
    arr = [(i % 2) for i in range(n)]
    cnt = min(20, max(0, n // 5))  # 依据 n 构造一个相对合理的 cnt

    # 保证 N 足够大，否则截断 arr
    if len(arr) >= N:
        arr = arr[:N - 1]

    ans = solve(arr, cnt)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模可按需修改
    main(100)