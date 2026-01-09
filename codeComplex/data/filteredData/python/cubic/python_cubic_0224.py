def main(n):
    # n controls the total length of three sequences R, G, B
    # We split n into r, g, b deterministically
    r = n // 3
    g = (n - r) // 2
    b = n - r - g
    if r < 1:
        r = 1
    if g < 1:
        g = 1
    if b < 1:
        b = 1

    # Deterministic data generation
    R = list(range(r, 0, -1))
    G = [(i * 2) % 1000 + 1 for i in range(g, 0, -1)]
    B = [(i * 3) % 1000 + 1 for i in range(b, 0, -1)]

    # Ensure descending order as in original (reverse=True)
    R = sorted(R, reverse=True)
    G = sorted(G, reverse=True)
    B = sorted(B, reverse=True)

    # Memoization table sized by r+1, g+1, b+1 instead of fixed 201
    mem = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def dp(i, j, k):
        p = (i == r) + (j == g) + (k == b)
        if p > 1:
            return 0
        if mem[i][j][k] != -1:
            return mem[i][j][k]
        ans = 0
        if i == r:
            ans = dp(i, j + 1, k + 1) + G[j] * B[k]
            mem[i][j][k] = ans
            return ans
        elif j == g:
            ans = dp(i + 1, j, k + 1) + R[i] * B[k]
        elif k == b:
            ans = dp(i + 1, j + 1, k) + R[i] * G[j]

        else:
            ans = max(
                dp(i + 1, j + 1, k) + R[i] * G[j],
                dp(i, j + 1, k + 1) + G[j] * B[k],
                dp(i + 1, j, k + 1) + R[i] * B[k],
            )
        mem[i][j][k] = ans
        return ans

    result = dp(0, 0, 0)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(30)