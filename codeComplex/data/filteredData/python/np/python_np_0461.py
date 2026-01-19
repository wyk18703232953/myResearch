def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # Deterministically construct x, y from n
    # Ensure x > 0, y > 0 and not both multiples of a large common factor
    x = 2 * n + 1
    y = 3 * n + 2

    import math
    g = math.gcd(x, y)
    h = lambda k: max(f(k, 0, x, y + x, g), f(k, 1, x, y + x, g))
    yy = y + x
    g = math.gcd(x, yy)
    res = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(res)

if __name__ == "__main__":
    main(10)