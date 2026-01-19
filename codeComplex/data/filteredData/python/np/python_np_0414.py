import math

def solve_with_generated_data(n):
    # Map n to original (n_rows, m_cols, values)
    if n <= 0:
        n_rows = 1
        m_cols = 1
    else:
        m_cols = (n % 7) + 1
        n_rows = max(1, n // m_cols)

    # Deterministic generation of arr with size n_rows x m_cols
    # Values are positive and spread so that threshold search is meaningful
    arr = [[(i * m_cols + j + 1) * (j + 2) for j in range(m_cols)] for i in range(n_rows)]

    m = m_cols
    N = (1 << m) - 1
    x = 1
    lo = 1
    hi = 1000000009
    ind = [0, 0]

    # First exponential search phase
    while True:
        l = {}
        freq = [0] * (1 << m)
        for i in range(n_rows):
            an = 0
            for j in range(m):
                if arr[i][j] >= x:
                    an += 1 << (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1

        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if (v1 | v2) == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break

        if ch:
            lo = x
            x = x * 2
        else:
            hi = x
            break

    # Binary search phase
    ans = lo
    while hi - lo > 1:
        x = (lo + hi) // 2
        l = {}
        freq = [0] * (1 << m)
        for i in range(n_rows):
            an = 0
            for j in range(m):
                if arr[i][j] >= x:
                    an += 1 << (m - j - 1)
            if freq[an] == 0:
                l[i] = an
            freq[an] = 1

        ch = 0
        for k1, v1 in l.items():
            for k2, v2 in l.items():
                if (v1 | v2) == N:
                    ch = 1
                    ind[0] = k1 + 1
                    ind[1] = k2 + 1
                    break
            if ch:
                break

        if ch:
            lo = x
        else:
            hi = x
    ans = lo

    if ind[0] == 0:
        print("1 1")
    else:
        print(ind[0], ind[1])

def main(n):
    solve_with_generated_data(n)

if __name__ == "__main__":
    main(100)