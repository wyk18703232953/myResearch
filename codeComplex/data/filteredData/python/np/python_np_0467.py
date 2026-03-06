import math

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(n, x, y, g):
    return max(f_func(n, 0, x, y, g), f_func(n, 1, x, y, g))

def main(n):
    # 映射规则：
    # n 为规模参数，构造一个三元组 (N, X, Y)
    # 保证 Y > 0 且与原逻辑兼容
    N = n + 5
    X = n * 2 + 3
    Y = n * 3 + 7

    g = math.gcd(X, Y)
    y_mod = Y + X  # 对应原代码中的 y += x;
    # h 需要使用更新后的 y，因此单独传入
    def h_local(k):
        return h_func(k, X, y_mod, g)

    result = N % g * h_local(N // g + 1) + (g - N % g) * h_local(N // g)
    print(result)

if __name__ == "__main__":
    main(10)