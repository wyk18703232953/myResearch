import math
import random

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(n, x, y, g):
    return max(f_func(n, 0, x, y, g), f_func(n, 1, x, y, g))

def main(n):
    # 根据规模 n 生成测试数据
    # 确保 x, y > 0 且与原逻辑一致
    random.seed(n)
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))
    
    g = math.gcd(x, y)
    y2 = y + x  # 对应原代码中 y += x 后的 y

    base = n // g
    r = n % g

    res = r * h_func(base + 1, x, y2, g) + (g - r) * h_func(base, x, y2, g)
    print(res)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数，可根据需要修改
    main(10)