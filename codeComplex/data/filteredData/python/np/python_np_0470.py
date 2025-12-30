import math
import random

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 生成规模为 n 的测试数据
    # 保证 x, y > 0 且互不为 0，避免除零问题
    # 可根据需要调整生成策略
    random.seed(0)
    x = random.randint(1, max(2, n))
    y = random.randint(1, max(2, n))

    # 若原题有其他约束，可在此调整 x, y
    g = math.gcd(x, y)
    h = lambda k: max(f_func(k, 0, x, y + x, g), f_func(k, 1, x, y + x, g))
    yy = y + x

    result = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模参数可自行修改
    main(10)