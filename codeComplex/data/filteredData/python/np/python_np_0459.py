import math
import random

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(k, x, y, g):
    return max(f_func(k, 0, x, y, g), f_func(k, 1, x, y, g))

def main(n):
    # 根据规模 n 生成测试数据：
    # 生成 1 <= x, y <= n，且至少有一个 > 0
    if n <= 0:
        raise ValueError("n 必须为正整数")
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    y2 = y + x

    t = n // g
    r = n % g

    ans = r * h_func(t + 1, x, y2, g) + (g - r) * h_func(t, x, y2, g)
    return ans

# 示例：直接运行本文件时给一个默认规模
if __name__ == "__main__":
    print(main(10))