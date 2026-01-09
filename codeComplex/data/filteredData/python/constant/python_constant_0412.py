def main(n):
    # Ensure n is at least 4 and even, because we need coordinates in pairs
    if n < 4:
        n = 4
    if n % 2 == 1:
        n += 1

    # Generate p: list of 2k coordinates within [0,100] after +100 shift
    # Use a simple deterministic pattern that keeps values in [0,100]
    half = n // 2
    p = []
    for i in range(half):
        x = (i * 3) % 100  # in [0,99]
        y = (i * 5) % 100  # in [0,99]
        p.append(x)
        p.append(y)
    # shift by +100 as in original code
    p = [v + 100 for v in p]

    # Generate d: also 2k coordinates, constructed from another pattern
    d = []
    for i in range(half):
        x = (i * 7 + 10) % 100  # in [0,99]
        y = (i * 11 + 20) % 100  # in [0,99]
        d.append(x)
        d.append(y)
    d = [v + 100 for v in d]

    minx = min(p[::2])
    maxx = max(p[::2])
    miny = min(p[1::2])
    maxy = max(p[1::2])

    grid = [[False] * 201 for _ in range(201)]
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            grid[x][y] = True

    minx = min(d[::2])
    maxx = max(d[::2])
    avgx = sum(d[::2]) // 4
    avgy = sum(d[1::2]) // 4
    span = (maxx - minx) // 2

    for x in range(minx, maxx + 1):
        height = span - abs(x - avgx)
        for y in range(avgy - height, avgy + height + 1):
            if 0 <= x <= 200 and 0 <= y <= 200 and grid[x][y]:
                # print('YES')
                pass
                return

    # print('NO')
    pass
if __name__ == "__main__":
    main(50)