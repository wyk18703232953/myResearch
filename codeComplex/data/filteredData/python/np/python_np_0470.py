def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(n, y, g, x):
    return max(f(n, 0, y, g, x), f(n, 1, y, g, x))

def original_logic(n, x, y):
    import math
    g = math.gcd(x, y)
    y_new = y + x
    h = lambda val: h_func(val, y_new, g, x)
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # Interpret n as the magnitude that controls the size of numeric inputs.
    # Deterministically construct (n_val, x_val, y_val) from n.
    # Ensure values are positive and scaled with n for complexity experiments.
    if n <= 0:
        n_val = 1
    else:
        n_val = n

    # Construct x and y deterministically from n
    x_val = n_val + 1          # simple linear function of n
    y_val = 2 * n_val + 3      # another linear function to avoid trivial gcd

    result = original_logic(n_val, x_val, y_val)
    print(result)

if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)