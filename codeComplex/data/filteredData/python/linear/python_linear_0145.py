def main(n):
    # n: length of array Ab, deterministically generated
    if n < 0:
        raise ValueError("n must be non-negative")

    # Deterministic generation of Ab: increasing-ish sequence
    # Example: Ab[i] = i % 5 + i // 3
    Ab = [i % 5 + i // 3 for i in range(n)]

    Un = []
    Al = [0]
    r = 0

    # First loop: same logic as original
    for i in range(n):
        Ab[i] = int(Ab[i])
        Al.append(max(Ab[i] + 1, Al[i]))

    # Second loop: propagate constraints backwards
    for i in range(n, -1, -1):
        if Al[i - 1] < Al[i] - 1:
            Al[i - 1] = Al[i] - 1

    # Third loop: compute Un and sum r
    for i in range(n):
        Un.append(Al[i + 1] - Ab[i] - 1)
        r += Un[-1]

    print(r)


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(10)
    main(100)