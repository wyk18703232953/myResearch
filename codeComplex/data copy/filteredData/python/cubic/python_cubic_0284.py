def main(n):
    # Map n to sizes of R, G, B, capped at 200 because dp is 201^3
    max_size = 200
    size = max(1, min(n, max_size))
    R = G = B = size

    # Deterministic data generation
    ra = [i % 1000 + 1 for i in range(R)]
    ga = [(i * 2) % 1000 + 1 for i in range(G)]
    ba = [(i * 3) % 1000 + 1 for i in range(B)]

    ra.sort(reverse=True)
    ga.sort(reverse=True)
    ba.sort(reverse=True)

    dp = [[[-1 for _ in range(201)] for _ in range(201)] for _ in range(201)]

    def solve(r, g, b):
        if dp[r][g][b] != -1:
            return dp[r][g][b]
        count = 0
        for i, j in zip((r, g, b), (R, G, B)):
            if i == j:
                count += 1
        if count >= 2:
            return 0

        res = -999
        if r != R and b != B:
            res = max(res, ra[r] * ba[b] + solve(r + 1, g, b + 1))
        if r != R and g != G:
            res = max(res, ra[r] * ga[g] + solve(r + 1, g + 1, b))
        if b != B and g != G:
            res = max(res, ba[b] * ga[g] + solve(r, g + 1, b + 1))

        dp[r][g][b] = res
        return res

    return solve(0, 0, 0)


if __name__ == "__main__":
    # Example call; change n to adjust input scale
    result = main(50)
    # print(result)
    pass