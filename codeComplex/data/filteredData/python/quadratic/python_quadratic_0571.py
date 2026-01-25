def main(n):
    # Interpret n as total grid size, choose closest factor pair (rows, cols)
    if n <= 0:
        return

    # Find factor pair (r, c) with r * c == n and |r - c| minimized
    r = 1
    c = n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            if abs(j - i) < abs(c - r):
                r, c = i, j

    # Now r, c play roles of original n, m
    n_rows = r
    m_cols = c

    if n_rows == 2:
        cval = 1
        way = []
        mult = 1
        for x in range(m_cols - 1, -1, -1):
            way.append(cval)
            cval += x * mult
            mult *= -1
        for x in way:
            print(1, x)
        for x in way[::-1]:
            print(2, x)

    elif n_rows == 1:
        cval = 1
        way = []
        mult = 1
        for x in range(m_cols - 1, -1, -1):
            way.append(cval)
            cval += x * mult
            mult *= -1
        for x in way:
            print(1, x)

    elif m_cols == 2:
        cval = 1
        way = []
        mult = 1
        for x in range(n_rows - 1, -1, -1):
            way.append(cval)
            cval += x * mult
            mult *= -1
        for x in way:
            print(x, 1)
        for x in way[:-1:-1]:
            print(x, 2)

    elif m_cols == 1:
        cval = 1
        way = []
        mult = 1
        for x in range(n_rows - 1, -1, -1):
            way.append(cval)
            cval += x * mult
            mult *= -1
        for x in way:
            print(x, 1)

    else:
        for x in range(n_rows // 2):
            for y in range(1, m_cols + 1):
                print(x + 1, y)
                print(n_rows - x, m_cols + 1 - y)
        if n_rows % 2 == 1:
            cval = 1
            way = []
            mult = 1
            for x in range(m_cols - 1, -1, -1):
                way.append(cval)
                cval += x * mult
                mult *= -1
            for x in way:
                print(n_rows // 2 + 1, x)


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(20)