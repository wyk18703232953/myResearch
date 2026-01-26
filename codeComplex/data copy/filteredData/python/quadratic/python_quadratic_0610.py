def main(n):
    # Interpret n as the size of array A; keep M and K as simple deterministic functions of n.
    # Ensure M is at least 1 and not larger than N.
    N = max(1, n)
    M = max(1, min(N, n // 2 + 1))
    K = n // 3 + 1

    # Deterministic construction of A based on n
    A = [(i * 2 - (n // 4)) for i in range(N)]

    bv = 0
    for ms in range(M):
        cv = 0
        for i in range(ms, N):
            v = A[i]
            if i % M == ms:
                v -= K
                cv = max(0, cv)
            cv += v
            bv = max(bv, cv)
    # print(bv)
    pass
if __name__ == "__main__":
    main(10)