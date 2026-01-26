def main(n):
    # Generate two deterministic binary strings of length n
    s0 = ''.join('0' if i % 3 != 0 else '1' for i in range(n))
    s1 = ''.join('0' if (i + 1) % 4 != 0 else '1' for i in range(n))
    s = [s0, s1]

    if n == 0:
        # print(0)
        pass
        return
    if n == 1:
        # print(0)
        pass
        return

    dp = [[0, 0, 0] for _ in range(n + 2)]

    for i in range(n - 2, -1, -1):
        dp[i] = [dp[i + 1][0]] * 3
        vals = [0, 0, 0, 0]
        if s[0][i] == '0' and s[0][i + 1] == '0' and s[1][i] == '0':
            vals[0] = dp[i + 1][2] + 1
        if s[0][i] == '0' and s[0][i + 1] == '0' and s[1][i + 1] == '0':
            vals[1] = dp[i + 2][0] + 1
        if s[1][i] == '0' and s[0][i + 1] == '0' and s[1][i + 1] == '0':
            vals[2] = dp[i + 2][0] + 1
        if s[0][i] == '0' and s[1][i] == '0' and s[1][i + 1] == '0':
            vals[3] = dp[i + 1][1] + 1
        dp[i][1] = max(dp[i + 1][0], vals[1])
        dp[i][2] = max(dp[i + 1][0], vals[2])
        dp[i][0] = max(dp[i][1], dp[i][2], *vals)

    result = max(dp[0])
    # print(result)
    pass
if __name__ == "__main__":
    main(10)