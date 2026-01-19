def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    import math
    # Deterministic generation of (n_value, x, y) based on n
    n_value = n
    x = n + 1
    y = 2 * n + 1
    g = math.gcd(x, y)
    h = lambda t: max(f(t, 0, x, y + x, g), f(t, 1, x, y + x, g))
    yy = y + x
    g2 = math.gcd(x, yy)
    return n_value % g2 * h(n_value // g2 + 1) + (g2 - n_value % g2) * h(n_value // g2)

if __name__ == "__main__":
    print(main(10))