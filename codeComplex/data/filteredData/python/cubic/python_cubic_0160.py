def calcdp_factory(a, dp):
    def calcdp(l, r):
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
    return calcdp

def solve(a):
    n = len(a) - 1  # because original code appends a 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    calcdp = calcdp_factory(a, dp)

    dp2 = [float('inf')] * (n + 1)
    dp2[0] = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if calcdp(i, j) > 0:
                dp2[j] = min(dp2[j], dp2[i] + 1)
    return dp2[n]

def generate_data(n):
    # Deterministic construction of array a of length n
    # Pattern: a[i] = (i % 3) + 1 to create repeated small integers
    a = [(i % 3) + 1 for i in range(n)]
    a.append(0)  # as in original code
    return a

def main(n):
    a = generate_data(n)
    result = solve(a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)