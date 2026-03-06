def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]


def h_func(n, x, y, g):
    return max(f_func(n, 0, x, y, g), f_func(n, 1, x, y, g))


def solve_one(n_val, x, y):
    import math
    g = math.gcd(x, y)
    y2 = y + x
    return n_val % g * h_func(n_val // g + 1, x, y2, g) + (g - n_val % g) * h_func(n_val // g, x, y2, g)


def main(n):
    # 解释输入规模映射（确定性构造）：
    # 使用 n 构造一组 (n_val, x, y)
    # n_val 随规模线性增长，x, y 按简单算术关系确定
    n_val = n
    x = n + 1
    y = 2 * n + 3

    # 运行一次核心算法以便做时间复杂度实验
    ans = solve_one(n_val, x, y)
    print(ans)


if __name__ == "__main__":
    main(100000)