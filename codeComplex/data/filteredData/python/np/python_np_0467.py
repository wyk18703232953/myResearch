import math
import random

def f_local(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    # y here is already x+y in the original logic
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
    return d[s]

def main(n):
    """
    n: problem scale, used to generate test data and as the original n in the logic.
    Returns the computed result.
    """
    # 生成与规模 n 对应的一组 (n, x, y)，这里原 n 就用参数 n，
    # x, y 生成为与 n 同量级的正整数。
    # 保证 gcd(x, y) 合理且不为 0。
    random.seed(1)  # 如需要可去掉固定 seed
    x = random.randint(1, max(1, 2 * n))
    y = random.randint(1, max(1, 2 * n))

    g = math.gcd(x, y)
    # 按原程序对 y 做修改：y += x
    y_mod = y + x

    def h(k):
        return max(f_local(k, 0, x, y_mod, g), f_local(k, 1, x, y_mod, g))

    # 原表达式：
    # print(n%g*h(n//g+1)+(g-n%g)*h(n//g))
    result = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    return result

# 示例：直接运行此文件时做一次调用（可根据需要保留或删除）
if __name__ == "__main__":
    print(main(10))