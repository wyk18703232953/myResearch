def main(n):
    # Map n to sizes of the three arrays in a balanced way
    rn = n
    gn = max(1, n // 2)
    bn = max(1, n // 3)

    # Deterministic generation of rr, gg, bb
    # Values are simple functions of index to keep them bounded yet non-trivial
    rr = [(i * 2 + 1) % 1000 for i in range(rn)]
    gg = [(i * 3 + 2) % 1000 for i in range(gn)]
    bb = [(i * 5 + 3) % 1000 for i in range(bn)]

    rr.sort(reverse=True)
    gg.sort(reverse=True)
    bb.sort(reverse=True)

    dp = [[[-1] * (bn + 1) for _ in range(gn + 1)] for _ in range(rn + 1)]
    dp[0][0][0] = 0
    ans = 0

    for i in range(rn + 1):
        for j in range(gn + 1):
            for k in range(bn + 1):
                pre = dp[i][j][k]
                if pre == -1:
                    continue
                if pre > ans:
                    ans = pre
                if i < rn and j < gn:
                    v = pre + rr[i] * gg[j]
                    if v > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = v
                if i < rn and k < bn:
                    v = pre + rr[i] * bb[k]
                    if v > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = v
                if j < gn and k < bn:
                    v = pre + gg[j] * bb[k]
                    if v > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = v

    return ans


if __name__ == "__main__":
    # Example deterministic call for timing/complexity experiments
    n = 30
    result = main(n)
    # print(result)
    pass