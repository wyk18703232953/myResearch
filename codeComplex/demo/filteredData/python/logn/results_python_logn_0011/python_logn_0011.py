def main(n):
    # Interpret n as the magnitude of the interval [l, r]
    # We construct a deterministic pair (l, r) such that:
    #   0 <= l <= r
    #   r - l is on the order of n
    # This preserves the original logical structure: a single test case with two integers.
    #
    # Deterministic construction:
    #   r = n
    #   l = n // 2
    # Ensures 0 <= l <= r for all non-negative n.
    l = n // 2
    r = n

    # Original core logic preserved
    for i in range(62, -1, -1):
        if ((1 << i) & l) ^ ((1 << i) & r):
            result = (1 << (i + 1)) - 1
            break

    else:
        result = 0

    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10**6)