def ms(x, y, d=0):
    return [[d] * y for _ in range(x)]


def ar(x, d=0):
    return [d] * x


INF = float("inf")

# Globals - will be (re)initialized in main for each n
dp = ms(501, 501)
dp2 = ar(501, INF)
arr = []


def calc_dp(l, r):
    assert l < r

    if l + 1 == r:
        dp[l][r] = arr[l]
        return dp[l][r]
    if dp[l][r] != 0:
        return dp[l][r]

    dp[l][r] = -1

    for i in range(l + 1, r):
        lf = calc_dp(l, i)
        rg = calc_dp(i, r)
        if lf > 0 and lf == rg:
            dp[l][r] = lf + 1
            return dp[l][r]

    return dp[l][r]


def solve(arr_local, n_local):
    global arr, dp2
    arr = arr_local
    # dp is already global and assumed initialized to 0 outside relevant range
    dp2[0] = 0

    for i in range(n_local):
        for j in range(i + 1, n_local + 1):
            v = calc_dp(i, j)
            if v > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)

    ans = dp2[n_local]
    return ans


def main(n):
    global dp, dp2, arr

    # Cap n to the maximum supported by the preallocated dp/dp2 size
    max_n = 500
    if n > max_n:
        n = max_n
    if n < 1:
        n = 1

    # Deterministic data generation: arr is a list of length n
    # Example pattern: arr[i] = (i % 5) + 1
    arr = [(i % 5) + 1 for i in range(n)]

    # Reinitialize dp and dp2 for a clean run
    dp = ms(501, 501, 0)
    dp2 = ar(501, INF)

    result = solve(arr, n)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)