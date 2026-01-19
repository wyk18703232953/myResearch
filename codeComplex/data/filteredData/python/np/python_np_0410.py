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

def build_A(N, M):
    A = []
    for i in range(N):
        row = []
        for j in range(M):
            val = (i + 1) * (j + 2)
            row.append(val)
        A.append(row)
    return A

def check_factory(A):
    N = len(A)
    if N == 0:
        return lambda m: False
    M = len(A[0]) if A[0] else 0

    def check(m):
        ok = [0] * N
        S = set()
        for i in range(N):
            row_mask = 0
            for j in range(M):
                if A[i][j] >= m:
                    row_mask |= 1 << j
            ok[i] = row_mask
            S.add(row_mask)
        full = (1 << M) - 1
        for bit1 in range(1 << M):
            if bit1 not in S:
                continue
            for bit2 in range(bit1, 1 << M):
                if bit2 in S and (bit1 | bit2) == full:
                    return True
        return False

    return check

def solve(A):
    N = len(A)
    if N == 0:
        return -1, -1
    M = len(A[0]) if A[0] else 0
    check = check_factory(A)
    res = bisearch_max(0, 10**9 + 1, check)
    ok = [0] * N
    S = set()
    D = {}
    for i in range(N):
        row_mask = 0
        for j in range(M):
            if A[i][j] >= res:
                row_mask |= 1 << j
        ok[i] = row_mask
        S.add(row_mask)
        D[row_mask] = i + 1
    full = (1 << M) - 1
    ans1, ans2 = -1, -1
    for bit1 in range(1 << M):
        if bit1 not in S:
            continue
        for bit2 in range(bit1, 1 << M):
            if bit2 in S and (bit1 | bit2) == full:
                ans1, ans2 = D[bit1], D[bit2]
                return ans1, ans2
    return ans1, ans2

def main(n):
    if n <= 0:
        N = 0
        M = 0
    else:
        N = max(1, n // 2)
        M = max(1, n - N)
    A = build_A(N, M)
    i1, i2 = solve(A)
    print(i1, i2)

if __name__ == "__main__":
    main(10)