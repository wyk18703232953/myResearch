import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def main(n):
    # Deterministic generation of x, y from n
    x = n + 1
    y = 2 * n + 1
    g = math.gcd(x, y)
    y_adj = y + x
    n_div_g = n // g
    n_mod_g = n % g
    res = n_mod_g * h(n_div_g + 1, x, y_adj, g) + (g - n_mod_g) * h(n_div_g, x, y_adj, g)
    print(res)

if __name__ == "__main__":
    main(10)