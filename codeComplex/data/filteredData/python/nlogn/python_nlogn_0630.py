def main(n):
    # Scale parameters deterministically based on n
    # m is length of ar and the third input array
    m = max(1, n)
    # First "line": n_input, m_input
    n_input = 1
    m_input = m

    # Second "line": ar array of length m
    # Deterministic construction
    ar = [i % 10 for i in range(m_input)]

    # Third "line": array of 1s and 2s of length m
    # Deterministic pattern, e.g., alternating 1 and 2
    third_array = [1 if i % 2 == 0 else 2 for i in range(m_input)]

    # Core logic from original program
    arc = []
    art = []
    res = []

    for idx, val in enumerate(third_array):
        if val == 1:
            art.append(ar[idx])
            res.append(0)

        else:
            arc.append(ar[idx])

    nt = 0
    if len(art) > 0:
        for i in arc:
            while nt != len(art) - 1 and abs(art[nt] - i) > abs(art[nt + 1] - i):
                nt += 1
            res[nt] += 1

    # Output in the same format as original code
    # print(" ".join(str(x) for x in res))
    pass
if __name__ == "__main__":
    main(10)