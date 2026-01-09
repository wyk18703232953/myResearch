def main(n):
    # Interpret n as the number of centers; radius r is fixed deterministically
    r = max(1, n // 10 + 1)
    # Deterministic generation of x_coord: spaced integers
    x_coord = [i * (r // 2 + 1) for i in range(1, n + 1)]

    d = {}
    results = []
    for i in x_coord:
        final = float(r)
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + ((4 * r * r) - ((i - check[0]) ** 2)) ** 0.5
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        results.append(final)

    # For reproducibility in experiments, we print the results
    for v in results:
        # print(v)
        pass
if __name__ == "__main__":
    main(10)