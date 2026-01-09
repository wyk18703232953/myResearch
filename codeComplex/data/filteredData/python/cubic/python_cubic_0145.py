def main(n):
    # Deterministic generation of input array a of length n
    # Example pattern: a[i] = (i % 3) + 1
    a = [(i % 3) + 1 for i in range(n)]

    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def solve(l, r):
        if dp[l][r]:
            return dp[l][r]
        if r - l == 1:
            dp[l][r] = (a[l], 1)
            return dp[l][r]
        tmp = 10 ** 9
        for i in range(l + 1, r):
            left = solve(l, i)
            right = solve(i, r)
            if left[0] == -1 or right[0] == -1:
                tmp = min(tmp, left[1] + right[1])
            elif left == right:
                val = left[0] + 1
                dp[l][r] = (val, 1)
                return dp[l][r]

            else:
                tmp = min(tmp, 2)
        dp[l][r] = (-1, tmp)
        return dp[l][r]

    solve(0, n)
    # print(dp[0][n][1])
    pass
if __name__ == "__main__":
    main(10)