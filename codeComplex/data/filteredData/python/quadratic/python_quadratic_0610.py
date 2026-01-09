def main(n):
    # Interpret n as N (size of array); choose M and K deterministically
    N = max(1, n)
    M = max(1, N // 3 + 1)
    K = N // 2 + 1

    # Deterministic construction of A
    A = [(i * 3 + 1) % (2 * N + 1) for i in range(N)]

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