def main(n):
    # Interpret n as total size of three arrays; split into r,g,b
    # Deterministic partition
    r = n // 3
    g = (n // 3) + (n % 3 > 0)
    b = n - r - g
    if r <= 0:
        r = 1
    if g <= 0:
        g = 1
    if b <= 0:
        b = 1

    # Deterministic data generation
    # Use simple arithmetic patterns to ensure repeatability
    R = [i + 1 for i in range(r)]
    G = [2 * (i + 1) for i in range(g)]
    B = [3 * (i + 1) for i in range(b)]

    R.sort()
    G.sort()
    B.sort()

    # DP array
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def recur(cr, cg, cb):
        if (cr + cg + cb) == cr or (cr + cg + cb) == cg or (cr + cg + cb) == cb:
            return 0
        if dp[cr][cg][cb]:
            return dp[cr][cg][cb]
        best = 0
        if cr > 0 and cg > 0:
            val = R[cr - 1] * G[cg - 1] + recur(cr - 1, cg - 1, cb)
            if val > best:
                best = val
        if cr > 0 and cb > 0:
            val = R[cr - 1] * B[cb - 1] + recur(cr - 1, cg, cb - 1)
            if val > best:
                best = val
        if cb > 0 and cg > 0:
            val = B[cb - 1] * G[cg - 1] + recur(cr, cg - 1, cb - 1)
            if val > best:
                best = val
        dp[cr][cg][cb] = best
        return best

    result = recur(r, g, b)
    # print(result)
    pass
if __name__ == "__main__":
    # Example scale; adjust n to change input size
    main(30)