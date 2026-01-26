def main(n):
    # Scale parameters based on n
    # n: base size -> array length and number of queries both depend on n
    N = max(1, n)
    M = max(1, n)

    # Deterministically generate w of length N
    # Use a simple pattern that creates some inversions
    w = [(i * 2 + (i % 3)) for i in range(N)]

    # Compute initial inversion parity
    c = 0
    for i in range(N):
        for j in range(i + 1, N):
            if w[i] > w[j]:
                c += 1
    c %= 2

    # Process M deterministic queries
    for j in range(M):
        # Deterministically generate [l, r] with 1-based indices
        # Use a simple wrap-around pattern depending on j and N
        l = (j % N) + 1
        r = ((j * 3) % N) + 1
        if l > r:
            l, r = r, l
        x = r - l + 1
        if x != 1 and (x * (x - 1) // 2) % 2:
            c = not c
        if c:
            # print("odd")
            pass

        else:
            # print("even")
            pass
if __name__ == "__main__":
    main(10)