import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve_case(n, x, y):
    g = math.gcd(x, y)
    h = lambda nn: max(f(nn, 0, x, y, g), f(nn, 1, x, y, g))
    y2 = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 通过 n 确定性生成 (n, x, y)
    # 保证 x, y > 0 且不过小
    base = max(1, n)
    x = 2 * base + 1
    y = 3 * base + 2
    return solve_case(base, x, y)

if __name__ == "__main__":
    # 示例：使用规模 n = 10 调用
    res = main(10)
    print(res)