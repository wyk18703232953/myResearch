def main(n):
    # Deterministically generate k and array a based on n
    # k must be > 0 to avoid modulo by zero
    k = n + 7  # simple deterministic relation, k >= 8 when n >= 1

    # Generate a list a of length n with varying magnitudes
    # Mix of small and larger numbers to exercise len(str(a[i]))
    a = [(i * i + 3 * i + 1) % (10 ** ((i % 10) + 1)) + 1 for i in range(1, n + 1)]

    b = []
    for i in range(11):
        c = {}
        for j in range(n):
            d = (a[j] * (10 ** i)) % k
            if d in c:
                c[d] += 1

            else:
                c[d] = 1
        b.append(c)

    s = 0
    for i in range(n):
        c = a[i] % k
        d = (k - c) % k
        length = len(str(a[i]))
        if d in b[length]:
            s += b[length][d]
        if (a[i] * (10 ** length)) % k == d:
            s -= 1

    # print(s)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(1000)