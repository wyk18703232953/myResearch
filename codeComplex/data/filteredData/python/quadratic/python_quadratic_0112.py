def main(n):
    # Generate deterministic n x n pattern for a and b
    # a is base pattern; b is a transformed version of a
    a = []
    for i in range(n):
        row = []
        for j in range(n):
            # deterministic character based on i, j, n
            val = (i * n + j) % 26
            row.append(chr(ord('A') + val))
        a.append(''.join(row))

    # Generate b as a transformed version of a to exercise the algorithm
    # For determinism, choose a transformation based on n modulo 8
    def rotate(d):
        # rotate 90 degrees clockwise on n x n matrix of chars in strings
        c = []
        for i in range(n):
            temp = ""
            for j in range(n):
                temp += d[j][n - i - 1]
            c.append(temp)
        return c

    def flip(d):
        # horizontal flip
        c = []
        for i in range(n):
            c.append(d[n - i - 1])
        return c

    transform_type = n % 8
    if transform_type == 0:
        b = a[:]  # identical
    elif transform_type == 1:
        b = rotate(a)
    elif transform_type == 2:
        b = rotate(rotate(a))
    elif transform_type == 3:
        b = rotate(rotate(rotate(a)))
    elif transform_type == 4:
        b = flip(a)
    elif transform_type == 5:
        b = rotate(flip(a))
    elif transform_type == 6:
        b = rotate(rotate(flip(a)))

    else:
        b = rotate(rotate(rotate(flip(a))))

    # Original logic using a and b
    def h(d):
        c = []
        for i in range(n):
            c.append(d[n - i - 1])
        return c

    def r(d):
        c = []
        for i in range(n):
            temp = ""
            for j in range(n):
                temp += d[j][n - i - 1]
            c.append(temp)
        return c

    yes = 0
    a_curr = a
    for _ in range(4):
        if a_curr == b:
            # print('YES')
            pass
            yes = 1
            break
        a_curr = r(a_curr)
    if yes == 0:
        a_curr = h(a_curr)
        for _ in range(4):
            if a_curr == b:
                # print('YES')
                pass
                yes = 1
                break
            a_curr = r(a_curr)
    if yes == 0:
        # print('NO')
        pass
if __name__ == "__main__":
    main(5)