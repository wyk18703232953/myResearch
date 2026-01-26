def main(n):
    # Interpret n as problem size: n elements, m = n queries
    # Deterministic construction of m, and the (x, d) pairs.
    m = n

    MAX = 0
    MIN = 10**18
    for i in range(n):
        l = i * (i + 1) // 2
        r = (n - 1 - i) * (n - i) // 2
        val = l + r
        if val > MAX:
            MAX = val
        if val < MIN:
            MIN = val

    ans = 0
    for i in range(m):
        # Deterministic generation of x, d based on i and n
        x = i - n // 2
        d = (i % 3) - 1  # cycles through -1, 0, 1
        ans += n * x
        if d >= 0:
            ans += d * MAX

        else:
            ans += d * MIN

    # Use integer division as in original code (Python 2 style)
    result = ans / n
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example call; you can change 10 to other sizes for experiments
    main(10)