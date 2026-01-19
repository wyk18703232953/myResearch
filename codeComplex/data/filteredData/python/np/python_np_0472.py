def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [
            max(d[0], d[1]),
            d[0] + n * g // y + (i * x % y < n * g % y),
        ]
    return d[s]


def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))


def main(n):
    # Deterministically generate x, y from n
    # Ensure x,y > 0 and not both multiples of a large common factor
    x = n + 1
    y = 2 * n + 3
    import math

    g = math.gcd(x, y)
    y2 = y + x
    return n % g * h(n // g + 1, x, y2, g) + (g - n % g) * h(n // g, x, y2, g)


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    print(result)