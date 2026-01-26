def main(n):
    # Interpret n as total length of all three arrays; split roughly equally
    if n <= 0:
        return 0
    R = max(1, n // 3)
    G = max(1, (n - R) // 2)
    B = max(1, n - R - G)

    # Deterministic data generation
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # Bounds: original code uses fixed 205; adapt to sizes but keep upper cap
    max_size = max(R, G, B, 1)
    cap = min(max_size, 205)

    # If sizes exceed 205, truncate to keep same DP complexity pattern
    R = min(R, cap)
    G = min(G, cap)
    B = min(B, cap)
    r = r[:R]
    g = g[:G]
    b = b[:B]

    # 3D DP with memoization, same logic as original
    dp = [[[-1] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    def recurser(x, y, z):
        if (x >= R and y >= G) or (y >= G and z >= B) or (z >= B and x >= R):
            return 0
        if dp[x][y][z] != -1:
            return dp[x][y][z]
        maxi = 0
        if x < R and y < G:
            val = r[x] * g[y] + recurser(x + 1, y + 1, z)
            if val > maxi:
                maxi = val
        if y < G and z < B:
            val = g[y] * b[z] + recurser(x, y + 1, z + 1)
            if val > maxi:
                maxi = val
        if z < B and x < R:
            val = r[x] * b[z] + recurser(x + 1, y, z + 1)
            if val > maxi:
                maxi = val
        dp[x][y][z] = maxi
        return maxi

    return recurser(0, 0, 0)


if __name__ == "__main__":
    # Example deterministic call for experimentation
    result = main(60)
    # print(result)
    pass