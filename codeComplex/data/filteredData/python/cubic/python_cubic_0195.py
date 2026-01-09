def main(n):
    # Generate deterministic input of size n
    # Original program: n is length of list a, read from stdin
    # Here: we construct a list a of length n deterministically
    if n <= 0:
        return
    a = [(i % 5) + 1 for i in range(n)]

    INF = 10001

    dp1 = [[-1] * n for _ in range(n)]
    dp3 = [[INF] * n for _ in range(n)]

    def cal(l, r):
        if l == r:
            dp1[l][r] = a[l]
            dp3[l][r] = 1
            return dp1[l][r]
        if dp1[l][r] != -1:
            return dp1[l][r]
        for i in range(l, r):
            if cal(l, i) == cal(i + 1, r) != 0:
                dp1[l][r] = dp1[l][i] + 1
                dp3[l][r] = 1
            dp3[l][r] = min(dp3[l][r], dp3[l][i] + dp3[i + 1][r])
        if dp1[l][r] == -1:
            dp1[l][r] = 0
        return dp1[l][r]

    cal(0, n - 1)
    # print(dp3[0][n - 1])
    pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)