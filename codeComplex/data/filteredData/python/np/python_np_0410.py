# -*- coding: utf-8 -*-

import random

INF = 10 ** 18
MOD = 10 ** 9 + 7

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

def main(n):
    """
    n: problem scale parameter, used here as N (number of rows).
       M (number of columns) and values in A are generated accordingly.
    """
    # Generate test data from n
    # N = n, M = min(n, 10) to keep bit-operations reasonable
    N = n
    M = max(1, min(n, 10))
    MAX_VAL = 10 ** 9

    # Generate A: N x M matrix with random integers in [0, MAX_VAL]
    random.seed(0)
    A = [[random.randint(0, MAX_VAL) for _ in range(M)] for _ in range(N)]

    def check(m):
        ok = [0] * N
        S = set()
        for i in range(N):
            for j in range(M):
                if A[i][j] >= m:
                    ok[i] |= 1 << j
            S.add(ok[i])
        full = (1 << M) - 1
        for bit1 in range(1 << M):
            for bit2 in range(bit1, 1 << M):
                if bit1 in S and bit2 in S:
                    if bit1 | bit2 == full:
                        return True
        return False

    res = bisearch_max(0, 10 ** 9 + 1, check)
    ok = [0] * N
    S = set()
    D = {}
    for i in range(N):
        for j in range(M):
            if A[i][j] >= res:
                ok[i] |= 1 << j
        S.add(ok[i])
        D[ok[i]] = i + 1
    full = (1 << M) - 1
    for bit1 in range(1 << M):
        for bit2 in range(bit1, 1 << M):
            if bit1 in S and bit2 in S:
                if bit1 | bit2 == full:
                    print(D[bit1], D[bit2])
                    return

if __name__ == "__main__":
    # Example: run with n = 5
    main(5)