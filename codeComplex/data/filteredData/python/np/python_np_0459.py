def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve_single_case(n, x, y):
    import math
    g = math.gcd(x, y)
    h = lambda nn: max(f(nn, 0, x, y + x, g), f(nn, 1, x, y + x, g))
    yy = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # Interpret n as the magnitude for generating one test case:
    # n controls the main parameter; x and y are deterministic functions of n.
    # Ensure positive values and some variability but fully deterministic.
    if n < 1:
        n = 1
    # Deterministic generation of x and y based on n
    x = 2 * n + 1
    y = 3 * n + 2
    result = solve_single_case(n, x, y)
    print(result)

if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)