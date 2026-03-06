def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def core_algorithm(n, x, y):
    import math
    g = math.gcd(x, y)
    y2 = y + x
    return n % g * h(n // g + 1, x, y2, g) + (g - n % g) * h(n // g, x, y2, g)

def main(n):
    # 映射：n 作为原程序中的 n，x 和 y 由 n 确定性生成
    # 保证 y != 0 且 x,y 不全为 0
    x = n + 1
    y = (2 * n + 3) if (2 * n + 3) != 0 else 1
    result = core_algorithm(n, x, y)
    print(result)

if __name__ == "__main__":
    main(10)