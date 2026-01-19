import math

def f(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def solve_single_case(n, x, y):
    g = math.gcd(x, y)
    h = lambda nv: max(f(nv, 0, x, y + x, g), f(nv, 1, x, y + x, g))
    y2 = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 构造 n 组测试数据，每组 (N, X, Y) 随 n 确定性变化
    total = 0
    for i in range(1, n + 1):
        N = i
        X = i + 1
        Y = i + 2
        total += solve_single_case(N, X, Y)
    print(total)

if __name__ == "__main__":
    main(10)