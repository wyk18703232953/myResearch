def check(mid: int, n: int, m: int, a, ans_container) -> bool:
    dic = {}
    for i in range(n):
        bit = 0
        for j in range(m):
            if a[i][j] >= mid:
                bit += 1
            bit <<= 1
        dic[bit >> 1] = i
    full = (1 << m) - 1
    for x, idx in dic.items():
        for y, idy in dic.items():
            if (x | y) == full:
                ans_container[0] = (idx + 1, idy + 1)
                return True
    return False


def main(n):
    # Map n to matrix dimensions
    # Choose m relatively small to keep 2^m manageable; for scaling time, grow n
    m = 5
    rows = max(1, n)

    # Deterministic data generation: a[i][j] = (i * (j + 1) + j) % 100
    a = [[(i * (j + 1) + j) % 100 for j in range(m)] for i in range(rows)]

    ans_container = [(-1, -1)]
    le = 0
    ri = 10**2  # upper bound consistent with value range in a
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid, rows, m, a, ans_container):
            le = mid + 1
        else:
            ri = mid - 1

    # Final answer from last successful mid
    print(ans_container[0][0], ans_container[0][1])


if __name__ == "__main__":
    main(1000)