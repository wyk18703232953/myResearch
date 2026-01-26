def is_on_line(a, b, c):
    return 1 if (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) == 0 else 0

def solve(n, a):
    if n <= 4:
        return 1
    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[0], a[1], a[i]):
            if len(line2) < 2:
                line2.append(i)

            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1

    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[0], a[2], a[i]):
            if len(line2) < 2:
                line2.append(i)

            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1

    line2 = []
    ok = 1
    for i in range(n):
        if not is_on_line(a[1], a[2], a[i]):
            if len(line2) < 2:
                line2.append(i)

            else:
                ok *= is_on_line(a[line2[0]], a[line2[1]], a[i])
                if ok == 0:
                    break
    if ok:
        return 1
    return 0

def generate_data(n):
    # Generate n deterministic 2D points.
    # Points are (i, i % 7) to mix collinear and non-collinear cases deterministically.
    a = [(i, i % 7) for i in range(n)]
    return n, a

def main(n):
    n, a = generate_data(n)
    res = solve(n, a)
    # print("Yes" if res == 1 else "No")
    pass
if __name__ == "__main__":
    main(10)