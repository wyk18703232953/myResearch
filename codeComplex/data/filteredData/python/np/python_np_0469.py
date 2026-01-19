import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # Deterministically construct (n_input, x, y) from n
    # Ensure positive values and y > 0
    n_input = max(1, n)
    x = max(1, 2 * n + 1)
    y = max(1, 3 * n + 2)

    g = math.gcd(x, y)
    h = lambda k: max(f(k, 0, x, y + x, g), f(k, 1, x, y + x, g))
    y2 = y + x
    g2 = math.gcd(x, y2)

    # Keep the original final expression structure, adapted to n_input, x, y2, g2
    result = n_input % g2 * h(n_input // g2 + 1) + (g2 - n_input % g2) * h(n_input // g2)
    print(result)
    return result

if __name__ == "__main__":
    # Example deterministic call
    main(10)