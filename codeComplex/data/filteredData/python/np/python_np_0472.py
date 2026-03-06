def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    limit = y // g
    ng_over_y = n * g // y
    ng_mod_y = n * g % y
    for i in range(limit):
        t0 = max(d[0], d[1])
        t1 = d[0] + ng_over_y + (1 if (i * x % y < ng_mod_y) else 0)
        d = [t0, t1]
    return d[s]

def h(n, y, g, x):
    v0 = f(n, 0, y, g, x)
    v1 = f(n, 1, y, g, x)
    return v0 if v0 > v1 else v1

def main(n):
    import math
    # Deterministic generation of original three integers (n0, x, y0)
    # Scale: n controls the magnitude
    n0 = n
    x = n + 1
    y0 = 2 * n + 3

    g = math.gcd(x, y0)
    y = y0 + x

    q = n0 // g
    r = n0 % g

    h_q = h(q, y, g, x)
    h_q1 = h(q + 1, y, g, x)

    ans = r * h_q1 + (g - r) * h_q
    print(ans)

if __name__ == "__main__":
    main(10)