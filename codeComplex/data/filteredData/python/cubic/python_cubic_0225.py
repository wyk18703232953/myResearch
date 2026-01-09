def main(n):
    # Interpret n as the common size of r, g, b
    if n <= 0:
        return
    r = g = b = n

    # Deterministic generation of rs, gs, bs
    rs = [i for i in range(1, r + 1)]
    gs = [i * 2 for i in range(1, g + 1)]
    bs = [i * 3 for i in range(1, b + 1)]

    rs.sort()
    gs.sort()
    bs.sort()

    ans = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(1, r + 1):
        for j in range(1, g + 1):
            ans[i][j][0] = ans[i - 1][j - 1][0] + rs[i - 1] * gs[j - 1]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(1, b + 1):
                new_len = bs[k - 1]
                if i == 0:
                    i_len = 0

                else:
                    i_len = ans[i - 1][j][k - 1] + rs[i - 1] * new_len
                if j == 0:
                    j_len = 0

                else:
                    j_len = ans[i][j - 1][k - 1] + gs[j - 1] * new_len
                if i > 0 and j > 0:
                    i_j_len = ans[i - 1][j - 1][k] + rs[i - 1] * gs[j - 1]

                else:
                    i_j_len = 0
                ans[i][j][k] = max(i_len, j_len, ans[i][j][k - 1], i_j_len)

    # print(ans[r][g][b])
    pass
if __name__ == "__main__":
    main(3)