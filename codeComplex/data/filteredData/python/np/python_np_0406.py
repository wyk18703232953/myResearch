def main(n):
    # Interpret n as: N rows, M = max(1, n % 10) columns
    # Ensure N >= 2 so that there are at least two rows to choose from
    N = max(2, n)
    M = max(1, n % 10)

    # Deterministic data generation:
    # L[i][j] = (i * 131 + j * 17 + n * 7) % (n + 10) + 1
    # This keeps values positive and bounded, fully determined by n.
    L = []
    for i in range(N):
        row = []
        for j in range(M):
            v = (i * 131 + j * 17 + n * 7) % (n + 10) + 1
            row.append(v)
        L.append(tuple(row))

    maxi = max(max(t) for t in L) + 1
    mini, res = max((min(t), i) for i, t in enumerate(L))
    res = res, res
    BITMASK = (1 << M)
    while True:
        mid = (maxi + mini) // 2
        if mid == mini:
            break
        masks = [None] * BITMASK
        for i, t in enumerate(L):
            tmask = 0
            for v in t:
                tmask *= 2
                if v >= mid:
                    tmask += 1
            if masks[tmask] is not None:
                continue
            masks[tmask] = i
            for k in range(BITMASK):
                if masks[k] is not None and k | tmask == BITMASK - 1:
                    res = masks[k], i
                    mini = mid = min(
                        max(a, b) for a, b in zip(L[res[0]], L[res[1]])
                    )
                    break
            else:
                continue
            break
        else:
            maxi = mid
    print(res[0] + 1, res[1] + 1)


if __name__ == "__main__":
    main(1000)