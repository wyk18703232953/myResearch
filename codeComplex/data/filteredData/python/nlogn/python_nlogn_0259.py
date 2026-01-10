def main(n):
    # Deterministic generation of n pairs (a, b)
    # a is non-decreasing, b varies in a patterned way
    c = []
    for i in range(n):
        a = i // 3           # creates groups with same a
        b = (i * 2) % (n + 1)  # deterministic variation of b
        c.append((a, b, i))

    if n == 0:
        print(-1, -1)
        return

    c.sort(key=lambda x: (x[0], -x[1]))
    a = c[0][1]
    b = c[0][2]
    an1 = -1
    an2 = -1
    for i in range(1, n):
        if c[i][1] <= a:
            an2 = b + 1
            an1 = c[i][2] + 1
            break
        else:
            a = c[i][1]
            b = c[i][2]
    print(an1, an2)


if __name__ == "__main__":
    main(10)