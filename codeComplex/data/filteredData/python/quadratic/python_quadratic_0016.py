def main(n):
    # Interpret n as: number of centers; radius r is fixed, coordinates deterministic
    r = 10
    x_coord = [i * 2 for i in range(1, n + 1)]

    d = {}
    outputs = []
    for i in x_coord:
        final = float(r)
        for j in range(i - r, i + r + 1):
            check = d.get(j, [-1, -1])
            if check[0] > 0:
                potential = check[1] + ((4 * r * r) - ((i - check[0]) ** 2)) ** 0.5
                final = max(potential, final)
        for j in range(i - r, i + r + 1):
            d[j] = (i, final)
        outputs.append(final)
    # print(" ".join(str(v) for v in outputs))
    pass
if __name__ == "__main__":
    main(5)