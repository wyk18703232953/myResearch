def bisearch_max(mn, mx, func):
    ok = mn
    ng = mx
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def solve(N, M, A):
    def check(m):
        ok = [0] * N
        S = set()
        for i in range(N):
            bitmask = 0
            row = A[i]
            for j in range(M):
                if row[j] >= m:
                    bitmask |= 1 << j
            ok[i] = bitmask
            S.add(bitmask)
        full = (1 << M) - 1
        for bit1 in range(1 << M):
            if bit1 not in S:
                continue
            for bit2 in range(bit1, 1 << M):
                if bit2 in S and (bit1 | bit2) == full:
                    return True
        return False

    res = bisearch_max(0, 10**9 + 1, check)

    ok = [0] * N
    S = set()
    D = {}
    for i in range(N):
        bitmask = 0
        row = A[i]
        for j in range(M):
            if row[j] >= res:
                bitmask |= 1 << j
        ok[i] = bitmask
        S.add(bitmask)
        D[bitmask] = i + 1

    full = (1 << M) - 1
    for bit1 in range(1 << M):
        if bit1 not in S:
            continue
        for bit2 in range(bit1, 1 << M):
            if bit2 in S and (bit1 | bit2) == full:
                return D[bit1], D[bit2]
    return -1, -1

def generate_data(n):
    if n < 1:
        n = 1
    M = min(8, max(1, n // 5))
    N = n
    A = [[(i * 31 + j * 17 + 7) % (10**9 + 7) for j in range(M)] for i in range(N)]
    return N, M, A

def main(n):
    N, M, A = generate_data(n)
    i, j = solve(N, M, A)
    print(i, j)

if __name__ == "__main__":
    main(50)