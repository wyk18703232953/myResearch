def main(n):
    # Generate deterministic test data based on n
    # Original code expects 4 blocks of n strings, each string length n, characters '0'/'1'
    s = [[None for _ in range(n)] for __ in range(4)]

    # Deterministic pattern for blocks 0,1,2 (originally read in 3 rounds with blank lines between)
    for i in range(3):
        for j in range(n):
            # Generate a binary string of length n deterministically
            # Example pattern: (i + j + k) % 2
            row = ['0'] * n
            for k in range(n):
                row[k] = '1' if (i + j + k) % 2 == 0 else '0'
            s[i][j] = ''.join(row)

    # Deterministic pattern for block 3 (originally read at the end)
    for j in range(n):
        row = ['0'] * n
        for k in range(n):
            row[k] = '1' if (j * 2 + k) % 3 == 0 else '0'
        s[3][j] = ''.join(row)

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
        Map = [s[lu][_][:] + s[ru][_][:] for _ in range(n)] + [s[ld][_][:] + s[rd][_][:] for _ in range(n)]
        cnt0, cnt1 = 0, 0
        for j in range(2 * n):
            row = Map[j]
            for k in range(2 * n):
                if (j + k) % 2:
                    if row[k] == '0':
                        cnt0 += 1

                    else:
                        cnt1 += 1

                else:
                    if row[k] == '1':
                        cnt0 += 1

                    else:
                        cnt1 += 1
        res = res if res < cnt0 else cnt0
        res = res if res < cnt1 else cnt1
    # print(res)
    pass
if __name__ == "__main__":
    main(5)