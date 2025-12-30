import math
import random

def f_impl(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve(n, x, y):
    g = math.gcd(x, y)
    def h(t):
        return max(f_impl(t, 0, x, y, g), f_impl(t, 1, x, y, g))
    y2 = y + x
    # 注意：原程序中 y 被修改为 y+x 后再使用，所以这里传入 y2
    # 但 f_impl 中用到的是修改后的 y，因此需要用 y2 调 h 内部的计算
    # 为保持语义一致，重新计算 h 使用 y2
    def h2(t):
        return max(f_impl(t, 0, x, y2, g), f_impl(t, 1, x, y2, g))
    return n % g * h2(n // g + 1) + (g - n % g) * h2(n // g)

def main(n):
    # 根据规模 n 生成测试数据 (n, x, y)
    # 保证 x, y 为正整数
    random.seed(0)
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))
    return solve(n, x, y)

if __name__ == "__main__":
    # 示例：调用 main，规模自定
    result = main(10)
    print(result)