import random

dp = []
a = []


def calcdp(l, r):
    global dp, a
    if l + 1 == r:
        dp[l][r] = a[l]
        return dp[l][r]
    if dp[l][r] != 0:
        return dp[l][r]
    dp[l][r] = -1
    for k in range(l + 1, r):
        la = calcdp(l, k)
        ra = calcdp(k, r)
        if la > 0 and la == ra:
            dp[l][r] = la + 1
    return dp[l][r]


def solve(n):
    dp2 = [float('inf')] * (n + 1)
    dp2[0] = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if calcdp(i, j) > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)
    return dp2[n]


def main(n):
    global dp, a
    # 生成规模为 n 的测试数据，这里使用 1~3 的随机整数
    a = [random.randint(1, 3) for _ in range(n)]
    a.append(0)

    dp = []
    ll = [0] * (n + 1)
    for _ in range(n + 1):
        dp.append(list(ll))

    ans = solve(n)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)