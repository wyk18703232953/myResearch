def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve_single_case(n, x, y):
    import math
    g = math.gcd(x, y)
    h = lambda k: max(f(k, 0, x, y, g), f(k, 1, x, y, g))
    y2 = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 使用确定性方式从 n 构造 (n, x, y)
    if n <= 0:
        return 0
    N = n
    x = 2 * N + 1
    y = 3 * N + 2
    return solve_single_case(N, x, y)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    print(main(10))