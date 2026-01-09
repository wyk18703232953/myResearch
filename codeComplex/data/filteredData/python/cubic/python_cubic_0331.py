def f(l, r, g, b, op):
    if (r == 0 and g == 0) or (r == 0 and b == 0) or (b == 0 and g == 0):
        return 0
    if op[r][g][b] != -1:
        return op[r][g][b]
    if r == 0:
        op[r][g][b] = l[1][g - 1] * l[2][b - 1] + f(l, r, g - 1, b - 1, op)
        return op[r][g][b]
    if g == 0:
        op[r][g][b] = l[0][r - 1] * l[2][b - 1] + f(l, r - 1, g, b - 1, op)
        return op[r][g][b]
    if b == 0:
        op[r][g][b] = l[0][r - 1] * l[1][g - 1] + f(l, r - 1, g - 1, b, op)
        return op[r][g][b]
    op[r][g][b] = max(
        l[1][g - 1] * l[2][b - 1] + f(l, r, g - 1, b - 1, op),
        l[0][r - 1] * l[2][b - 1] + f(l, r - 1, g, b - 1, op),
        l[0][r - 1] * l[1][g - 1] + f(l, r - 1, g - 1, b, op),
    )
    return op[r][g][b]


def main(n):
    if n <= 0:
        n = 1
    r = n
    g = n
    b = n
    a_r = [i for i in range(1, r + 1)]
    a_g = [(i * 2) for i in range(1, g + 1)]
    a_b = [(i * 3) for i in range(1, b + 1)]
    l = [sorted(a_r), sorted(a_g), sorted(a_b)]
    op = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    return f(l, r, g, b, op)


if __name__ == "__main__":
    # example: run with n = 3
    result = main(3)
    # print(result)
    pass