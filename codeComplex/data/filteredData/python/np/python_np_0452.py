def f_factory(x, y):
    def f(n, s):
        d = [-n, -n]
        d[s] = 0
        for i in range(y):
            d = [max(d[0], d[1]), d[0] + n // y + (i * x % y < n % y)]
        return d[s]
    return f

def main(n):
    if n < 3:
        n = 3
    # Deterministically construct inputs n0, x, y from n
    # Ensure x, y > 0 and not both multiples of each other trivially
    n0 = n
    x = n // 2 + 1
    y = n // 3 + 2
    # Recompute with original logic
    g = __import__("math").gcd(x, y)
    n1 = n0 // g
    x1 = x // g
    y1 = (x + y) // g
    r = n0 % g
    f = f_factory(x1, y1)
    h = lambda nn: max(f(nn, 0), f(nn, 1))
    result = h(n1 + 1) * r + h(n1) * (g - r)
    print(result)

if __name__ == "__main__":
    main(10)