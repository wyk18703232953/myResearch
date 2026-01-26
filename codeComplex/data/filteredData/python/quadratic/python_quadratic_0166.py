def main(n):
    # Interpret n as N (length of P); K is fixed and small so that A[0..255] is enough
    N = n
    if N <= 0:
        return

    # Deterministic construction of K
    # Choose a small K so that pn-j stays within [0,255] for generated P
    K = 5

    # Deterministic construction of P:
    # Make sure each pn stays in [0,255] so it fits in the fixed A array
    # Simple pattern: P[i] = (i * 7) % 256
    P = [(i * 7) % 256 for i in range(N)]

    A = [None] * 256
    A[0] = 0
    for i in range(N):
        pn = P[i]
        if A[pn] is None:
            for j in range(K - 1, -1, -1):
                if pn < j:
                    continue
                if A[pn - j] is None:
                    A[pn - j] = pn - j
                    break

                else:
                    if A[pn - j] + K - 1 >= pn:
                        break
            for jj in range(j, -1, -1):
                A[pn - jj] = A[pn - j]
    # print(*[A[P[i]] for i in range(N)])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)