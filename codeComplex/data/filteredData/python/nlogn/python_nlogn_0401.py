def main(n):
    # Deterministically generate n 2D points as floats
    # Input structure in original code:
    # first line: number of points (ignored after read)
    # following lines: "x y" per point
    points = []
    for i in range(n):
        # Simple deterministic generation: some variety with division and modulus
        x = float(i - n / 2)
        y = float((i * 2) % (n + 1) - n / 3)
        points.append([x, y, i])

    # Core logic from original program
    from math import hypot

    l = points
    l.sort(key=lambda xyi: abs(xyi[0]))
    res = ['1'] * len(l)
    x, y, _ = l.pop()
    while l:
        dx, dy, i = l.pop()
        a, b, u, v = x + dx, y + dy, x - dx, y - dy
        if hypot(a, b) < hypot(u, v):
            x, y = a, b
        else:
            x, y, res[i] = u, v, '-1'
    print(' '.join(res))


if __name__ == "__main__":
    main(10)