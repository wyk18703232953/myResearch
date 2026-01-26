def main(n):
    # Interpret n as N (length of the list). M is unused in the core logic.
    N = max(1, n)
    M = N  # placeholder to keep original input structure (N, M)

    # Deterministic generation of za with length N
    # Example: strictly increasing sequence so that sorting descending has effect
    za = [(i * 2 + 3) for i in range(N)]

    za.sort(reverse=True)

    re = 0
    for i in range(N - 1):
        a = za[i]
        b = za[i + 1]
        g = b
        if g >= a:
            t = a - 1
            if t < 1:
                t = 1
            re += g - t
            za[i + 1] = t
            re += a - 1

        else:
            re += g
    # print(re)
    pass
if __name__ == "__main__":
    main(10)