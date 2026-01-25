def main(n):
    # Deterministically generate k and data based on n
    # k cycles between 1 and 10, but at least 1
    k = (n % 10) + 1
    # data values are in [0, 255] to match mapping size
    # simple deterministic pattern: i * 7 mod 256
    data = [(i * 7) % 256 for i in range(n)]

    sol = []
    mapping = [(-1, 1000)] * 256
    for x in data:
        if mapping[x][0] == -1:
            for i in range(max(x - k + 1, 0), x + 1):
                if mapping[i][0] == -1:
                    if i > 0 and mapping[i - 1][1] + (x - i + 1) <= k:
                        p = mapping[i - 1][1] + 1
                        for j in range(i, x + 1):
                            mapping[j] = (mapping[i - 1][0], p)
                            p += 1
                    else:
                        p = 1
                        for j in range(i, x + 1):
                            mapping[j] = (i, p)
                            p += 1
                    break
        sol.append(mapping[x][0])

    print(' '.join(map(str, sol)))


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)