def main(n):
    MOD = 10**9 + 7

    # Deterministic generation of the original input structure:
    # original: n, then n lines each a string "s" or something else
    # Here: build a list of length n, pattern depends only on n and index
    s = []
    for i in range(n):
        # Alternate "s" and "f" in a deterministic way
        if i % 2 == 0:
            s.append("s")

        else:
            s.append("f")

    dps = [[0] * (n + 3) for _ in range(n + 1)]
    dpf = [[0] * (n + 3) for _ in range(n + 1)]

    for k in range(n + 1):
        dps[0][k] = 1

    for pos, char in enumerate(s):
        if char == "s":
            for depth in range(pos + 2):
                dps[pos + 1][depth] = (
                    dpf[pos][depth]
                    - dpf[pos][depth - 1]
                    + dps[pos][pos]
                    - dps[pos][depth - 1]
                )
                dps[pos + 1][depth] += dps[pos + 1][depth - 1]
                dps[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD

        else:
            for depth in range(1, pos + 2):
                dpf[pos + 1][depth] = (
                    dpf[pos][depth - 1]
                    - dpf[pos][depth - 2]
                    + dps[pos][pos]
                    - dps[pos][depth - 2]
                )
                dpf[pos + 1][depth] += dpf[pos + 1][depth - 1]
                dpf[pos + 1][depth] %= MOD

            for p in range(pos + 2, n + 1):
                dpf[pos + 1][p] += dpf[pos + 1][p - 1]
                dpf[pos + 1][p] %= MOD

    ans = dps[n][n] % MOD
    return ans


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(10)
    # print(result)
    pass