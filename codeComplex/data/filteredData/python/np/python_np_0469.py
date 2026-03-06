import math

def f_func(n_local, s, y, g, x):
    d = [-n_local, -n_local]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n_local * g // y + (i * x % y < n_local * g % y)]
    return d[s]

def h_func(n_local, y, g, x):
    return max(f_func(n_local, 0, y, g, x), f_func(n_local, 1, y, g, x))

def main(n):
    # Deterministic generation of original inputs (n_orig, x, y)
    # Scale x and y linearly with n to make the workload depend on n.
    n_orig = n
    x = n + 1
    y = 2 * n + 3

    g = math.gcd(x, y)
    y_mod = y + x

    h_n_div_g_plus_1 = h_func(n_orig // g + 1, y_mod, g, x)
    h_n_div_g = h_func(n_orig // g, y_mod, g, x)

    result = n_orig % g * h_n_div_g_plus_1 + (g - n_orig % g) * h_n_div_g
    print(result)

if __name__ == "__main__":
    main(1000)