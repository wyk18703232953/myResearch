def main(n):
    # Interpret n as N; choose K as a simple deterministic function of N
    N = n
    if N <= 0:
        return
    K = max(1, N // 4 + 1)
    # Generate P as a deterministic list of length N with values in [0, 255]
    # Ensure values are within 0..255 since A has length 256
    P = [((i * 7 + 3) % 256) for i in range(N)]

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
    main(10)