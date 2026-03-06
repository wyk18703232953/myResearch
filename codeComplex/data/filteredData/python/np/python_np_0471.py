import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def core_logic(n, x, y):
    g = math.gcd(x, y)
    y2 = y + x
    return n % g * h(n // g + 1, x, y2, g) + (g - n % g) * h(n // g, x, y2, g)

def main(n):
    x = 2 * n + 1
    y = 3 * n + 2
    result = core_logic(n, x, y)
    print(result)

if __name__ == "__main__":
    main(1000)