import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h(n, x, y, g):
    return max(f(n, 0, x, y, g), f(n, 1, x, y, g))

def main(n):
    # 使用 n 构造确定性的 (n, x, y)，保持原程序单组输入结构
    # 约束：x > 0, y > 0 且与 n 有一定关系以保证可扩展性
    if n <= 0:
        n_val = 1
    else:
        n_val = n

    # 构造与规模相关的 x, y
    x = n_val + 1
    y = 2 * n_val + 3

    g = math.gcd(x, y)
    yy = y + x

    t1 = n_val // g + 1
    t2 = n_val // g
    res = n_val % g * h(t1, x, yy, g) + (g - n_val % g) * h(t2, x, yy, g)
    print(res)
    return res

if __name__ == "__main__":
    main(1000)