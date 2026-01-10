def main(n):
    # Interpret n as the length of the list
    if n < 2:
        return 0

    # Deterministic generation of a, b, c and list d
    # a: arbitrary starting value
    a = 1
    # b: length of list
    b = n
    # c: choose a valid index in [1, b-1]
    c = max(1, min(b - 1, n // 2))

    # Generate b integers deterministically
    d = [(i * 3 + 7) % (5 * n + 11) for i in range(b)]
    d_sorted = sorted(d)

    e = d_sorted[c - 1]
    f = d_sorted[c]
    result = f - e
    print(result)
    return result


if __name__ == "__main__":
    main(10)