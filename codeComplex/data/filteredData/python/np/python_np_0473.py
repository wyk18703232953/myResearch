import math
import random

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve(n, x, y):
    g = math.gcd(x, y)
    h = lambda t: max(f(t, 0, x, y + x, g), f(t, 1, x, y + x, g))
    yy = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 根据规模 n 生成测试数据
    # 使得 x, y 与 n 同数量级
    random.seed(1)
    x = random.randint(1, max(1, 2 * n))
    y = random.randint(1, max(1, 2 * n))
    # 确保 y + x 在 f 中使用时合理（原逻辑中直接 y += x）
    ans = solve(n, x, y)
    print(ans)

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)