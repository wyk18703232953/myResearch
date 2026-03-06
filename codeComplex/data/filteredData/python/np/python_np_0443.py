def bisect_f(f, lo, hi):
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if f(mid):
            lo = mid
        else:
            hi = mid
    return lo


def solve(N, M, arrs):
    def isPossible(target):
        possible = set()
        for arr in arrs:
            mask = 0
            for pos, x in enumerate(arr):
                if x >= target:
                    mask += 1 << pos
            possible.add(mask)
        allMask = (1 << M) - 1
        for mask1 in possible:
            for mask2 in possible:
                if mask1 | mask2 == allMask:
                    return (mask1 << 8) + mask2
        return 0

    lo = min(arrs[0])
    hi = 10 ** 9 + 1
    index = bisect_f(isPossible, lo, hi)

    mask1, mask2 = divmod(isPossible(index), 1 << 8)
    ans = [-1, -1]
    for i, arr in enumerate(arrs):
        mask = 0
        for pos, x in enumerate(arr):
            if x >= index:
                mask += 1 << pos
        if mask == mask1:
            ans[0] = str(i + 1)
        if mask == mask2:
            ans[1] = str(i + 1)
    return " ".join(ans)


def main(n):
    # Define scaling: for given n, build a roughly square-ish matrix
    # N = n, M = max(1, min(8, n)) to keep bitmasks within 8 bits as original code assumes
    N = max(1, n)
    M = max(1, min(8, n))

    # Deterministic data generation:
    # arrs[i][j] = (i+1)*10 + j
    arrs = [[(i + 1) * 10 + j for j in range(M)] for i in range(N)]

    ans = solve(N, M, arrs)
    print(ans)


if __name__ == "__main__":
    main(5)