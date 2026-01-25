def main(n):
    # n controls the size of the problem
    # define n and m based on n to keep them proportional and scalable
    if n <= 0:
        print(0)
        return

    m = 2 * n

    # deterministic generation of c and a based on n and m
    # c: length n, increasing-ish values
    c = [(i * 3 + 1) % (2 * n + 1) + i // 3 for i in range(n)]
    # a: length m, different but deterministic pattern
    a = [(i * 5 + 2) % (3 * n + 2) + i // 2 for i in range(m)]

    c_i = 0
    a_i = 0
    bought = 0
    while c_i != n and a_i != m:
        if a[a_i] >= c[c_i]:
            a_i += 1
            c_i += 1
            bought += 1
        else:
            c_i += 1
    print(bought)


if __name__ == "__main__":
    main(10)