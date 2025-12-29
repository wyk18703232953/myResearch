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
    # 根据规模 n 生成测试数据:
    # 保证 x, y 为正整数，且不为 0，范围与 n 同量级
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    h = lambda k: max(f_func(k, 0, x, y + x, g),
                      f_func(k, 1, x, y + x, g))
    yy = y + x

    # 使用与原程序相同的逻辑
    ans = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)