import math
import random

def f_local(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 根据规模 n 生成测试数据:
    # x, y 为正整数，且不为 0，做一个简单的随机生成示例：
    # 让 x, y 在 [1, 2n] 范围内，避免为 0。
    random.seed(0)
    x = random.randint(1, max(1, 2 * n))
    y = random.randint(1, max(1, 2 * n))

    g = math.gcd(x, y)
    y2 = y + x  # 对应原代码中 y += x 后的 y

    def h(k):
        return max(f_local(k, 0, x, y2, g), f_local(k, 1, x, y2, g))

    n_div_g = n // g
    n_mod_g = n % g
    ans = n_mod_g * h(n_div_g + 1) + (g - n_mod_g) * h(n_div_g)
    print(ans)

if __name__ == "__main__":
    # 示例：给定一个规模 n 运行主函数
    main(10)