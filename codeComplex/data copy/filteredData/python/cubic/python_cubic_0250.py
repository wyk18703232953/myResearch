def main(n):
    # Interpret n as the size of each color set
    ri = gi = bi = n

    # Deterministically generate sorted lists rr, gr, br of length n
    # Use simple arithmetic so the data is fully determined by n
    rr = list(range(1, ri + 1))
    gr = list(range(2, 2 * gi + 2, 2))[:gi]
    br = [(i * 3) for i in range(1, bi + 1)]

    rr.sort()
    gr.sort()
    br.sort()

    dp = [[[-1] * (bi + 1) for _ in range(gi + 1)] for __ in range(ri + 1)]

    def area(r, g, b):
        if dp[r + 1][g + 1][b + 1] != -1:
            return dp[r + 1][g + 1][b + 1]
        ans = 0
        if r >= 0 and g >= 0:
            ans = max(ans, rr[r] * gr[g] + area(r - 1, g - 1, b))
        if r >= 0 and b >= 0:
            ans = max(ans, rr[r] * br[b] + area(r - 1, g, b - 1))
        if b >= 0 and g >= 0:
            ans = max(ans, br[b] * gr[g] + area(r, g - 1, b - 1))
        dp[r + 1][g + 1][b + 1] = ans
        return ans

    result = area(ri - 1, gi - 1, bi - 1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(5)