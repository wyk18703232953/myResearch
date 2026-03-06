def f(n, s, g, x, y):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]


def solve_single_case(n_val, x, y):
    import math
    g = math.gcd(x, y)
    h = lambda nn: max(f(nn, 0, g, x, y), f(nn, 1, g, x, y))
    y2 = y + x
    q = n_val // g
    r = n_val % g
    return r * h(q + 1) + (g - r) * h(q)


def main(n):
    # n controls the scale of generated inputs.
    # We deterministically generate (n) test cases, each with parameters (n_i, x_i, y_i)
    # where their magnitudes scale with n.

    results = []
    for i in range(1, n + 1):
        # Deterministic generation of n_val, x, y that scales with n and i
        n_val = i * n + i  # grows roughly as n^2
        x = i + 1          # simple increasing x
        y = 2 * i + 3      # simple increasing y, not proportional to x to keep gcd varied

        res = solve_single_case(n_val, x, y)
        results.append(res)

    # Aggregate output in a simple deterministic way to avoid huge prints
    # For time-complexity experiments, usually running time is what's measured,
    # so we just print something dependent on all results.
    total = sum(results)
    print(total)


if __name__ == "__main__":
    # Example call; adjust n for different input scales.
    main(1000)