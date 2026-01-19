def main(n):
    # Interpret n as the list length N
    N = max(1, n)
    # Deterministically construct L, H, d based on N
    L = N * (N // 2)
    H = N * N * 2
    d = max(1, N // 3)
    # Deterministically construct list l of length N
    l = [(i * 2 + 3) % (3 * N + 7) for i in range(N)]

    e = 0
    for mask in range(1 << N):
        k = []
        for j in range(N):
            if (mask >> j) & 1:
                k.append(l[j])
        if k:
            maz = max(k)
            mins = min(k)
            sums = sum(k)
            if L <= sums <= H and maz - mins >= d:
                e += 1
    print(e)


if __name__ == "__main__":
    main(10)