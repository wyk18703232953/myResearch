def main(n):
    # Map n to problem parameters deterministically
    # Ensure at least 1 to avoid degenerate bit-iteration edge issues
    n = max(1, int(n))

    # Define search bounds and difficulty gap based on n
    l = n
    r = 3 * n
    x = max(1, n // 3)

    # Deterministic generation of Cs: strictly increasing sequence
    Cs = [i * 2 + 1 for i in range(n)]  # [1,3,5,...]

    probs = 0
    for i in range(1, 2 ** n):
        currsub = [Cs[j] for j in range(n) if (i & (1 << j))]
        probs += (len(currsub) > 1 and l <= sum(currsub) <= r and currsub[-1] - currsub[0] >= x)

    print(probs)


if __name__ == "__main__":
    main(10)