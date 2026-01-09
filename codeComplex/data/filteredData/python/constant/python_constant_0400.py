def get(a, x):
    return (a[0][x] == "0") + (a[1][x] == "0")


def core(a):
    n = len(a[0])
    if n == 1:
        return 0
    dp = [[-1, -1, -1] for _ in range(n)]
    z = get(a, 0)
    dp[0][z] = 0
    for i in range(1, n):
        z = get(a, i)
        if z == 0:
            dp[i][0] = max(dp[i - 1])
        elif z == 1:
            dp[i][0] = dp[i - 1][2] + 1
            dp[i][1] = max(dp[i - 1])
        elif z == 2:
            dp[i][0] = max(dp[i - 1][1] + 1, dp[i - 1][2] + (i != 1))
            dp[i][1] = dp[i - 1][2] + 1
            dp[i][2] = max(dp[i - 1])
    return max(dp[-1])


def main(n):
    if n <= 0:
        return 0
    row0 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
    row1 = ''.join('1' if (i // 2) % 2 == 0 else '0' for i in range(n))
    a = [row0, row1]
    ans = core(a)
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)