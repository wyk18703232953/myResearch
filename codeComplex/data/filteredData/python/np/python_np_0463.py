def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(n, y, g, x):
    return max(f(n, 0, y, g, x), f(n, 1, y, g, x))

def main(n):
    # 映射规则：
    # 原程序有三个输入 n, x, y
    # 这里将实验规模参数 n 映射为：
    #   n_input = n
    #   x = 2 * n + 1
    #   y = 3 * n + 2
    # 这样三个参数都与规模 n 线性相关，便于时间复杂度实验
    import math

    if n <= 0:
        return 0

    n_input = n
    x = 2 * n + 1
    y = 3 * n + 2

    g = math.gcd(x, y)
    y2 = y + x  # 对应原代码中的 y = y + x

    h = lambda k: h_func(k, y2, g, x)

    result = n_input % g * h(n_input // g + 1) + (g - n_input % g) * h(n_input // g)
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 的大小进行实验
    print(main(10))