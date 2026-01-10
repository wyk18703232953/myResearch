def main(n):
    # Interpret n as the number of rows; choose k deterministically as n//2 (at least 1)
    if n <= 0:
        print(0)
        return
    k = max(1, n // 2)

    # Generate deterministic data: list of [score, id, extra...] with fixed width
    # We need at least 2 columns; more columns won't change core logic
    # l[i][0] is the primary key used in original algorithm
    l = []
    for i in range(n):
        # Primary value with some pattern to create ties around k
        val0 = (i // 3)  # creates blocks of equal first elements
        val1 = i         # secondary value to distinguish rows
        l.append([val0, val1])

    # Core logic from original code
    c = 0
    l.sort(reverse=True)
    a = l[k - 1][0]
    x = k - 1
    y = k - 1

    for i in range(k - 2, -1, -1):
        if l[i][0] == a:
            x = i
        else:
            break

    for i in range(k, n):
        if l[i][0] == a:
            y = i
        else:
            break

    d = k - 1 - x
    d = y - d

    for i in range(y, x - 1, -1):
        if l[i] == l[d]:
            c += 1

    print(c)


if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(10)