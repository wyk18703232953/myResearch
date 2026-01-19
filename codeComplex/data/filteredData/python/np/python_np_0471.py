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
    # 映射 n 为原程序中的 (n, x, y)
    # 保持确定性：给定 n，总是得到相同的三元组
    if n < 1:
        n_eff = 1
    else:
        n_eff = n

    # 原始 n 的规模
    orig_n = n_eff

    # 构造 x, y：与规模相关但完全确定
    x = n_eff + 1
    y = 2 * n_eff + 3

    g = math.gcd(x, y)
    y_total = y + x

    res = orig_n % g * h(orig_n // g + 1, x, y_total, g) + (g - orig_n % g) * h(orig_n // g, x, y_total, g)
    print(res)

if __name__ == "__main__":
    # 示例：调用 main，输入规模可自行调整
    main(10)