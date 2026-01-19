def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # Deterministic generation of the original three "inputs" n, x, y from a single scale n.
    # Ensure x, y > 0 and not both multiples of each other trivially, to keep gcd logic meaningful.
    base = max(1, n)
    x = base + 1
    y = 2 * base + 3
    import math
    g = math.gcd(x, y)
    def h(t):
        return max(f(t, 0, y + x, g, x), f(t, 1, y + x, g, x))
    yy = y + x
    k = base
    result = k % g * h(k // g + 1) + (g - k % g) * h(k // g)
    print(result)

if __name__ == "__main__":
    main(1000)