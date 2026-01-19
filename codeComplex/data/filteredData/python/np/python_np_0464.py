import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def main(n):
    # 将 n 映射为原始程序中的 n, x, y
    # 保证 gcd(x, y) 不为 0，且规模随 n 增长
    N = max(1, n)
    x = 2 * N + 1
    y = 3 * N + 2
    g = math.gcd(x, y)
    y2 = y + x
    return N % g * h(N // g + 1, x, y2, g) + (g - N % g) * h(N // g, x, y2, g)

if __name__ == "__main__":
    # 示例调用
    for n in range(1, 6):
        print(n, main(n))