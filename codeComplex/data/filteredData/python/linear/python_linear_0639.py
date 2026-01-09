def main(n):
    # Generate deterministic max_degs of length n
    # Pattern: degrees cycle through [1,2,3,1,2,3,...]
    max_degs = [(i % 3) + 1 for i in range(n)]

    B = [[i + 1, x] for i, x in enumerate(max_degs) if x >= 2]
    S = [[i + 1, x] for i, x in enumerate(max_degs) if x < 2]

    if 2 + sum(b - 2 for _, b in B) < len(S):
        # print('NO')
        pass
        return

    # print('YES', len(B) + min(len(S), 2) - 1)
    pass
    # print(n - 1)
    pass

    # B edges
    for k in range(len(B) - 1):
        i, x = B[k]
        i_n, _ = B[k + 1]
        # print(i, i_n)
        pass
        B[k][1] -= 1
        B[k + 1][1] -= 1

    k = 0
    for i, (s_idx, _) in enumerate(S):
        if i == 0:
            # print(B[0][0], s_idx)
            pass
            B[0][1] -= 1
        elif i == 1:
            # print(B[-1][0], s_idx)
            pass
            B[-1][1] -= 1

        else:
            while B[k][1] == 0:
                k += 1
            # print(B[k][0], s_idx)
            pass
            B[k][1] -= 1


if __name__ == "__main__":
    main(10)