def main(n):
    # Map n to sizes of R, G, B in a simple deterministic way
    # Ensure they are at least 1
    R = max(1, n)
    G = max(1, n // 2 if n >= 2 else 1)
    B = max(1, n // 3 if n >= 3 else 1)

    # Deterministic generation of r, g, b
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    def calc(nr, ng, nb):
        if dp[nr][ng][nb] != -1:
            return dp[nr][ng][nb]
        res = 0
        if nr < R and ng < G:
            res = max(res, calc(nr + 1, ng + 1, nb) + r[nr] * g[ng])
        if nr < R and nb < B:
            res = max(res, calc(nr + 1, ng, nb + 1) + r[nr] * b[nb])
        if ng < G and nb < B:
            res = max(res, calc(nr, ng + 1, nb + 1) + g[ng] * b[nb])
        dp[nr][ng][nb] = res
        return res

    result = calc(0, 0, 0)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)