import math
import random

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 生成测试数据：x, y 为与 n 同量级的正整数
    # 保证 x, y > 0
    random.seed(0)
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    y_sum = y + x

    def h(t):
        return max(f_func(t, 0, x, y_sum, g),
                   f_func(t, 1, x, y_sum, g))

    result = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(result)


# 示例：调用 main，规模 n 可在此调整
if __name__ == "__main__":
    main(10)