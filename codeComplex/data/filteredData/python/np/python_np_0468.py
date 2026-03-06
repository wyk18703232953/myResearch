import math

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(val, x, y, g):
    return max(f_func(val, 0, x, y, g), f_func(val, 1, x, y, g))

def core_logic(n, x, y):
    g = math.gcd(x, y)
    y_total = y + x
    part1 = n % g * h_func(n // g + 1, x, y_total, g)
    part2 = (g - n % g) * h_func(n // g, x, y_total, g)
    return part1 + part2

def main(n):
    # Deterministic generation of x, y from n
    # Ensure x, y > 0 and not both zero; also avoid trivial gcd=0
    x = n + 1
    y = 2 * n + 3
    return core_logic(n, x, y)

if __name__ == "__main__":
    # Example deterministic call
    result = main(1000)
    print(result)