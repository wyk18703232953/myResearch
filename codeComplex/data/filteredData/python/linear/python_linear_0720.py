def main(n):
    # n controls the scale: n = length of b, m = length of g = n
    if n <= 0:
        return
    m = n

    # Deterministic generation of b and g based on n
    # b: increasing with some variation
    b = [(i * 3 + 1) % (2 * n + 3) for i in range(n)]
    # Ensure at least one reasonably large value so logic is exercised
    if n >= 1:
        b[0] = 2 * n

    # g: values around n with a deterministic pattern
    g = [(i * 5 + 2) % (3 * n + 5) for i in range(m)]
    if m >= 1:
        g[0] = n

    first_max = 0
    second_max = 0
    for i in range(n):
        if b[i] < first_max and b[i] > second_max:
            second_max = b[i]
        if b[i] >= first_max:
            second_max = first_max
            first_max = b[i]

    first_min = min(g)

    if first_max > first_min:
        print(-1)
    else:
        total = sum(b) * m + sum(g) - m * first_max + (first_max - second_max) * (first_min != first_max)
        print(total)


if __name__ == "__main__":
    main(10)