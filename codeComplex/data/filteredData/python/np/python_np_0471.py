import math
import random

def f_func(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def main(n):
    # 生成测试数据：随机生成 x, y（正整数）
    # 确保 x, y > 0 且不要太大，避免过慢；可按需调整范围
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    h = lambda k: max(f_func(k, 0, x, y + x, g), f_func(k, 1, x, y + x, g))
    yy = y + x

    # 原逻辑中 y 被替换为 y + x，因此使用 yy 作为新的 y
    # 但 gcd 是使用原始 x, y 计算的
    # 按原程序结构重写
    y2 = yy
    res = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(res)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改或由外部驱动
    main(10)