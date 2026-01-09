def main(n):
    # Interpret n as size of arrays b and g, with n >= 2 to have meaningful second_max
    if n < 2:
        n = 2

    # Deterministic generation of b and g
    # b: increasing sequence with some variation
    b = [(i * 3) % (2 * n + 1) + i for i in range(n)]
    # Ensure at least some spread
    b[0] = 1
    b[1] = 2

    # g: shifted version to control first_min relation
    g = [b[i] + (i % 3) for i in range(n)]

    # Set m as function of n
    m = n

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
        # print(-1)
        pass

    else:
        total = sum(b) * m + sum(g) - m * first_max + (first_max - second_max) * (first_min != first_max)
        # print(total)
        pass
if __name__ == "__main__":
    main(10)