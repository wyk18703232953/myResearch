def main(n):
    # Map n to sizes of three arrays (r, g, b)
    # Simple deterministic partition: r = n, g = n, b = n
    r = n
    g = n
    b = n

    # Deterministic generation of arrays R, G, B
    R = [(i * 2 + 1) for i in range(r)]
    G = [(i * 3 + 2) for i in range(g)]
    B = [(i * 5 + 3) for i in range(b)]

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    # Allocate dp with dimensions (r+5) x (g+5) x (b+5)
    dp = [[[0 for _ in range(b + 5)] for _ in range(g + 5)] for _ in range(r + 5)]

    sys.setrecursionlimit(2000000)

    def solve(i, j, k):
        x, y, z = 0, 0, 0
        if dp[i][j][k]:
            return dp[i][j][k]
        if i < r and j < g:
            x = R[i] * G[j] + solve(i + 1, j + 1, k)
        if i < r and k < b:
            y = R[i] * B[k] + solve(i + 1, j, k + 1)
        if j < g and k < b:
            z = G[j] * B[k] + solve(i, j + 1, k + 1)
        mx = x
        if y > mx:
            mx = y
        if z > mx:
            mx = z
        dp[i][j][k] = mx
        return mx

    result = solve(0, 0, 0)
    # print(result)
    pass
if __name__ == "__main__":
    import sys

    # Example deterministic call; adjust n to change input scale
    main(5)