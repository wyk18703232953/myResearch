import math

def f_func(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def h_func(n_val, x, y, g):
    return max(f_func(n_val, 0, x, y, g), f_func(n_val, 1, x, y, g))

def core_logic(n, x, y):
    g = math.gcd(x, y)
    y_mod = y + x
    return n % g * h_func(n // g + 1, x, y_mod, g) + (g - n % g) * h_func(n // g, x, y_mod, g)

def main(n):
    x = n + 1
    y = 2 * n + 1
    result = core_logic(n, x, y)
    print(result)

if __name__ == "__main__":
    main(10)