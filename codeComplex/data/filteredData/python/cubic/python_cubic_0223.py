def main(n):
    # Interpret n as the size of each color list
    R = n
    G = n
    B = n

    # Deterministic data generation
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # Shift arrays to be 1-indexed
    r = [0] + r
    g = [0] + g
    b = [0] + b

    R += 1
    G += 1
    B += 1

    dp = [[[0] * B for _ in range(G)] for __ in range(R)]
    res = 0

    for i in range(R):
        for j in range(G):
            for k in range(B):
                tmp = 0
                if i > 0 and j > 0:
                    tmp = max(tmp, dp[i - 1][j - 1][k] + r[i] * g[j])
                if i > 0 and k > 0:
                    tmp = max(tmp, dp[i - 1][j][k - 1] + r[i] * b[k])
                if j > 0 and k > 0:
                    tmp = max(tmp, dp[i][j - 1][k - 1] + g[j] * b[k])
                dp[i][j][k] = tmp
                if tmp > res:
                    res = tmp

    # print(res)
    pass
if __name__ == "__main__":
    main(500)
    # print(111)
    pass