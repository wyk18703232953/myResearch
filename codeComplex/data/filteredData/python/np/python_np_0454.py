def f_local(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]


def h_local(n, y, g, x):
    return max(f_local(n, 0, y, g, x), f_local(n, 1, y, g, x))


def core_algorithm(n, x, y):
    import math
    g = math.gcd(x, y)
    y += x
    h_val1 = h_local(n // g + 1, y, g, x)
    h_val2 = h_local(n // g, y, g, x)
    return n % g * h_val1 + (g - n % g) * h_val2


def main(n):
    # Deterministic generation of n, x, y from single scale parameter n
    # Ensure positive values and some variability
    if n <= 0:
        n_val = 1
    else:
        n_val = n

    # Generate x and y deterministically based on n
    # Keep them reasonably sized but dependent on n for scaling
    x = 2 * n_val + 3
    y = 3 * n_val + 5

    result = core_algorithm(n_val, x, y)
    print(result)


if __name__ == "__main__":
    # Example call with a chosen scale; adjust as needed for experiments
    main(10)