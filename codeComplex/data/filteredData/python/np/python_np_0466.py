import math
import random

def f_func(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def h_func(n_val, x, y, g):
    return max(f_func(n_val, 0, x, y, g), f_func(n_val, 1, x, y, g))

def main(n):
    # 生成测试数据：(n, x, y)
    # 保证 x, y > 0 且与 n 有一定规模关系
    # 示例策略：x, y 在 [1, 2n] 范围内随机生成，并确保 gcd(x, y) != 0
    if n <= 0:
        raise ValueError("n must be positive")

    x = random.randint(1, 2 * n)
    y = random.randint(1, 2 * n)

    g = math.gcd(x, y)
    y2 = y + x  # 对应原始代码中 y += x

    # 计算结果
    q, r = divmod(n, g)
    h_q1 = h_func(q + 1, x, y2, g)
    h_q  = h_func(q,     x, y2, g)
    ans = r * h_q1 + (g - r) * h_q

    print(ans)

if __name__ == "__main__":
    # 示例：指定规模 n
    main(10)