def main(n):
    # Interpret n as the number of rows; choose m as a small fixed dimension
    m = 5
    # Deterministically generate matrix A of size n x m
    # Values are chosen to give a reasonable spread for binary search
    A = [[(i * m + j) % 1000 for j in range(m)] for i in range(n)]

    # Initialize bounds for binary search
    lo = 1 << 32
    hi = -1 << 32
    for i in range(n):
        row_min = min(A[i])
        row_max = max(A[i])
        if row_min < lo:
            lo = row_min
        if row_max > hi:
            hi = row_max

    best = -1
    ans = [-1, -1]

    def possible(x):
        nonlocal best, ans
        M = [-1] * (1 << m)

        for i in range(n):
            mask = 0
            for j in range(m):
                if A[i][j] >= x:
                    mask |= (1 << j)
            M[mask] = i

        full_mask = (1 << m) - 1
        for m0 in range(1 << m):
            if M[m0] == -1:
                continue
            for m1 in range(1 << m):
                if M[m1] == -1:
                    continue
                if (m0 | m1) == full_mask:
                    if best < x:
                        best = x
                        ans = [M[m0] + 1, M[m1] + 1]
                    return True
        return False

    possible(hi)
    possible(lo)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if possible(mid):
            lo = mid
        else:
            hi = mid

    print(*ans)


if __name__ == "__main__":
    main(10)