def main(n):
    # Interpret n as total cells, construct a near-square grid n = rows * cols
    if n <= 0:
        return
    # Choose rows as floor(sqrt(n)), cols as ceil(n / rows)
    rows = int(n ** 0.5)
    if rows == 0:
        rows = 1
    cols = (n + rows - 1) // rows
    # Trim extra cells by reducing cols if rows*cols > n
    while rows * cols > n and cols > 1:
        cols -= 1
    # Now apply original logic with deterministic (rows, cols)
    r, c = rows, cols
    for i in range(r // 2):
        for j in range(c):
            sys.stdout.write('{} {}\n'.format(i + 1, j + 1))
            sys.stdout.write('{} {}\n'.format(r - i, c - j))
    if r % 2:
        for j in range(c // 2):
            sys.stdout.write('{} {}\n'.format(r // 2 + 1, j + 1))
            sys.stdout.write('{} {}\n'.format(r // 2 + 1, c - j))
        if c % 2:
            sys.stdout.write('{} {}\n'.format(r // 2 + 1, c // 2 + 1))


if __name__ == "__main__":
    import sys
    main(10)