def main(n):
    # Interpret n as N (number of tuples), and derive M deterministically
    # Ensure M >= 1
    M = max(1, n % 7 + 1)
    N = n

    # Deterministically generate L: list of N tuples, each of length M
    # Values are positive integers constructed deterministically from i, j
    L = [tuple((i * (j + 1) + j * j + 1) % (5 * M + 7) + 1 for j in range(M)) for i in range(N)]

    if N == 0:
        return

    maxi = max(max(t) for t in L) + 1
    mini, res = max((min(t), i) for i, t in enumerate(L))
    res = (res, res)
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
                if masks[k] is not None and (k | tmask) == BITMASK - 1:
                    res = (masks[k], i)
                    mini = mid = min(max(a, b) for a, b in zip(L[res[0]], L[res[1]]))
                    break
            else:
                continue
            break
        else:
            maxi = mid

    print(res[0] + 1, res[1] + 1)


if __name__ == "__main__":
    main(10)