def bitcount(m):
    return bin(m).count('1')


def solve(n, x, y):
    if x > y:
        x, y = y, x
    mm1 = range(1, 1 << y, 2)
    vbases = [
        ((~(m1 >> (y - x)) & ~m1 & ((1 << x) - 1)) << y) | m1
        for m1 in mm1
        if m1 & (m1 >> x) == 0
    ]

    def btail(m):
        return bitcount(m & ((1 << (n % (x + y))) - 1))

    return max(bitcount(m) * (n // (x + y)) + btail(m) for m in vbases)


def main(n):
    # Deterministically generate x, y from n with 1 <= x <= y <= 15
    x = max(1, (n % 5) + 1)
    y = max(x, (n % 10) + 5)
    y = min(y, 15)
    # Ensure x <= y and both positive
    if x > y:
        x, y = y, x
    if x == 0:
        x = 1
    if y == 0:
        y = 1
    print(solve(n, x, y))


if __name__ == "__main__":
    main(20)