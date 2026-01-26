def main(n):
    # Generate deterministic test data based on n
    # s is a 4 x n matrix of characters ('0' or '1')
    s = [["" for _ in range(n)] for __ in range(4)]
    for i in range(4):
        for j in range(n):
            # Simple deterministic pattern using i and j
            if (i * n + j) % 2 == 0:
                s[i][j] = '0'

            else:
                s[i][j] = '1'

    res = int(1e13)
    for i in range(24):
        perm = [0, 1, 2, 3]
        L = [0] * 4
        tmp = i
        for j in range(4):
            L[j] = tmp % (4 - j)
            tmp //= (4 - j)
        LL = [0] * 4
        for j in range(4):
            LL[j] = perm[L[j]]
            for k in range(L[j], 3 - j):
                perm[k] = perm[k + 1]
        lu, ru, ld, rd = LL[0], LL[1], LL[2], LL[3]

        # Construct the 2n x 2n board
        Map = [s[lu][_][:] + s[ru][_][:] for _ in range(n)] + \
              [s[ld][_][:] + s[rd][_][:] for _ in range(n)]

        cnt0, cnt1 = 0, 0
        for j in range(2 * n):
            for k in range(2 * n):
                if (j + k) % 2:
                    if Map[j][k] == '0':
                        cnt0 += 1

                    else:
                        cnt1 += 1

                else:
                    if Map[j][k] == '1':
                        cnt0 += 1

                    else:
                        cnt1 += 1
        res = min(res, cnt0, cnt1)
    # print(res)
    pass
if __name__ == "__main__":
    main(5)