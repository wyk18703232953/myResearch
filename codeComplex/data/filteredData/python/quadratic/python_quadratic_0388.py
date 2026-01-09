def main(n):
    # Interpret n as both dimensions of the grid (a = b = n)
    a = n
    b = n

    # Deterministically generate a grid of 'B' and 'W'
    # Pattern: center a square block of 'B's whose size scales with n
    # Ensure at least one 'B' exists
    size = max(1, n // 3)
    start = (n - size) // 2
    end = start + size

    grid = []
    for i in range(a):
        row = []
        for j in range(b):
            if start <= i < end and start <= j < end:
                row.append('B')

            else:
                row.append('W')
        grid.append(''.join(row))

    c = []
    e = []
    for i in range(a):
        d = grid[i]
        for j in range(b):
            if d[j] == "B":
                c = c + [i]
                e = e + [j]

    if not c:  # fallback in case n is 0
        # print(1, 1)
        pass
        return

    p = min(c)
    p1 = min(e)
    p2 = max(c)
    plus = (p2 - p) // 2
    p3 = p + plus + 1
    p4 = p1 + plus + 1
    # print(p3, p4)
    pass
if __name__ == "__main__":
    main(5)