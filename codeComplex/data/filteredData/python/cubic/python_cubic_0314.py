def main(n):
    r = n
    g = n
    b = n
    R = [i for i in range(1, r + 1)]
    G = [i * 2 for i in range(1, g + 1)]
    B = [i * 3 for i in range(1, b + 1)]
    R.sort()
    G.sort()
    B.sort()
    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(rr, gg, bb):
        if (rr == 0 and gg == 0) or (gg == 0 and bb == 0) or (bb == 0 and rr == 0):
            return 0
        if dp[rr][gg][bb] == -1:
            if rr == 0:
                ans = G[gg - 1] * B[bb - 1] + solve(rr, gg - 1, bb - 1)
            elif gg == 0:
                ans = R[rr - 1] * B[bb - 1] + solve(rr - 1, gg, bb - 1)
            elif bb == 0:
                ans = G[gg - 1] * R[rr - 1] + solve(rr - 1, gg - 1, bb)

            else:
                ans = max(
                    G[gg - 1] * B[bb - 1] + solve(rr, gg - 1, bb - 1),
                    G[gg - 1] * R[rr - 1] + solve(rr - 1, gg - 1, bb),
                    R[rr - 1] * B[bb - 1] + solve(rr - 1, gg, bb - 1),
                )
            dp[rr][gg][bb] = ans
        return dp[rr][gg][bb]

    return solve(r, g, b)


if __name__ == "__main__":
    # print(main(3))
    pass