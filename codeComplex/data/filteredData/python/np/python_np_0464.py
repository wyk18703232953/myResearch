import math

def f_func(n_val, s, x, y, g):
    y_div_g = y // g
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y_div_g):
        d = [max(d[0], d[1]),
             d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def h_func(n_val, x, y, g):
    return max(f_func(n_val, 0, x, y, g), f_func(n_val, 1, x, y, g))

def core_algorithm(n, x, y):
    g = math.gcd(x, y)
    y_new = y + x
    return n % g * h_func(n // g + 1, x, y_new, g) + (g - n % g) * h_func(n // g, x, y_new, g)

def main(n):
    # Interpret n as the scale parameter.
    # We deterministically generate x and y as functions of n.
    # Ensure x and y are positive and not both zero.
    x = n + 1
    y = 2 * n + 3
    return core_algorithm(n, x, y)

if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    result = main(10**5)
    print(result)