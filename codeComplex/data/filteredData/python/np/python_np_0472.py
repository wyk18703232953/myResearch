import math
import random

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 x, y 为与 n 同数量级的正整数
    # 保证 x, y > 0
    random.seed(0)
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    def h(k):
        return max(f_func(k, 0, x, y + x, g), f_func(k, 1, x, y + x, g))

    yy = y + x
    # 注意：f_func 和 h 使用的是更新后的 y (= yy)
    # 为了与原始逻辑一致，重新计算 g 对应新的 y
    g = math.gcd(x, yy)
    def h2(k):
        return max(f_func(k, 0, x, yy, g), f_func(k, 1, x, yy, g))

    result = n % g * h2(n // g + 1) + (g - n % g) * h2(n // g)
    print(result)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)