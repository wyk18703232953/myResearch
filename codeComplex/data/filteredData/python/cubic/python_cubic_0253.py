def main(n):
    # Map n to sizes of the three arrays (keep them reasonably balanced)
    # Ensure at least size 1 for non-zero n
    if n <= 0:
        r = g = b = 0

    else:
        r = max(1, n // 3)
        g = max(1, (n + 1) // 3)
        b = max(1, (n + 2) // 3)

    # Deterministic generation of R, G, B (already sorted descending)
    R = [r * 3 - i for i in range(1, r + 1)]
    G = [g * 3 - i * 2 for i in range(1, g + 1)]
    B = [b * 3 - i * 3 for i in range(1, b + 1)]

    # DP memoization table
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
    return result


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(60)