def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def solve(n, x, y):
    import math
    g = math.gcd(x, y)
    y2 = y + x
    return n % g * h(n // g + 1, x, y2, g) + (g - n % g) * h(n // g, x, y2, g)

def main(n):
    # 确定性生成输入规模：
    # n 控制三个整数的大小等级：
    #   N = n
    #   X = 2n + 1
    #   Y = 3n + 2
    # 保证正数且规模随 n 线性增长
    if n <= 0:
        N = 1
        X = 1
        Y = 2
    else:
        N = n
        X = 2 * n + 1
        Y = 3 * n + 2
    ans = solve(N, X, Y)
    print(ans)

if __name__ == "__main__":
    main(10)