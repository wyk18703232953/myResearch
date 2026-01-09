def main(n):
    # Interpret n as grid size: n x n
    # Also generate pairs deterministically based on n
    if n <= 0:
        return (0, 0)

    # Original variables: n, m, k, ints, pairs
    grid_n = n
    grid_m = n

    # Deterministically generate k and ints
    # Here k is even, and we create k/2 pairs
    k = max(2, (n // 2) * 2)
    ints = []
    for i in range(k):
        if i % 2 == 0:
            # x coordinate in [1, grid_n]
            val = (i // 2) % grid_n + 1

        else:
            # y coordinate in [1, grid_m]
            val = (i // 2 * 2 + 1) % grid_m + 1
        ints.append(val)

    pairs = []
    for i in range(0, len(ints), 2):
        x = ints[i]
        y = ints[i + 1]
        pairs.append((x, y))

    last_tree = (1, 1)
    maxd = 0
    mult = grid_m * grid_n

    for i in range(1, grid_n + 1):
        for j in range(1, grid_m + 1):
            md = mult
            for x, y in pairs:
                d = abs(i - x) + abs(j - y)
                if d < md:
                    md = d
            if md > maxd:
                last_tree = (i, j)
                maxd = md

    return last_tree


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    result = main(100)
    # print(result[0], result[1])
    pass