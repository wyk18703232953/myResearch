def main(n):
    # Deterministic generation of t and n pairs (a, b)
    # Scale: n = number of (a, b) pairs
    t = n // 3 + 1  # simple deterministic function of n

    l = []
    # Generate pairs so that a is increasing and b has some variation
    for i in range(n):
        a = i * 2 + 1
        b = (i % 5) + 1
        x = a - b / 2
        y = a + b / 2
        l.append([x, y])

    l.sort()
    c = 0
    for i in range(n - 1):
        if l[i + 1][0] - l[i][1] > t:
            c += 2
        elif l[i + 1][0] - l[i][1] == t:
            c += 1
    print(c + 2)


if __name__ == "__main__":
    main(10)