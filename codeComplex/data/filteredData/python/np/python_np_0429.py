hell=1000000007
id1 = 0
id2 = 0
a = []

def check(n, m, x):
    global id1, id2, a
    b = [0] * (1 << m)
    idx = [0] * (1 << m)
    for i in range(n):
        mask = 0
        for j in range(m):
            if a[i][j] >= x:
                mask = mask ^ (1 << j)
        b[mask] = 1
        idx[mask] = i + 1
    full = (1 << m) - 1
    for i in range(1 << m):
        if b[i]:
            for j in range(1 << m):
                if b[j]:
                    mask = i | j
                    if mask == full:
                        id1 = idx[i]
                        id2 = idx[j]
                        return 1
    return 0

def main(n):
    global id1, id2, a
    id1 = 0
    id2 = 0
    a = []

    if n <= 0:
        return

    # Scale: n = number of rows; m = min(8, n) to keep 2^m manageable
    m = 8 if n >= 8 else n

    # Deterministic data generation: a[i][j] are integers in a structured pattern
    # Values are in [1, hell), but small enough to make binary search meaningful
    for i in range(n):
        row = []
        for j in range(m):
            # Simple deterministic arithmetic pattern
            val = (i + 1) * (j + 2) + (i // 2) + (j * j)
            if val >= hell:
                val = val % hell
            row.append(val)
        a.append(row)

    lo = 0
    hi = hell
    while hi - lo > 0:
        mid = (hi + lo + 1) // 2
        if check(n, m, mid):
            lo = mid
        else:
            hi = mid - 1
    check(n, m, lo)
    # Keep the original observable behavior: print indices
    print(id1, id2)

if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)