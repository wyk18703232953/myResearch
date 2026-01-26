def main(n):
    # Deterministically generate inputs based on n
    # a, b, x, y, z are linear functions of n to scale the problem size
    a = 2 * n + 3
    b = 3 * n + 5
    x = n + 1
    y = 2 * n + 1
    z = n // 2 + 1

    r = 0

    yellow = 2 * x
    blue = 3 * z
    green = y

    if a > yellow:
        a -= yellow

    else:
        r += abs(a - yellow)
        a = 0

    if b > blue:
        b -= blue

    else:
        r += abs(b - blue)
        b = 0

    if a > green:
        a -= green

    else:
        r += abs(a - green)

    if b > green:
        b -= green

    else:
        r += abs(b - green)

    # print(r)
    pass
if __name__ == "__main__":
    main(10)