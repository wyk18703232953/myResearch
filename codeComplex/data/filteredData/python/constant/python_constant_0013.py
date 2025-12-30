import math
import random

def gett(a, b, c):
    delta = b ** 2 - 4 * a * c
    # 理论上原题中参数保证 delta >= 0，这里做一下保护
    if delta < 0:
        return float('nan')
    sqrt_delta = delta ** 0.5
    t1 = (-b + sqrt_delta) / (2 * a)
    t2 = (-b - sqrt_delta) / (2 * a)
    return min(t1, t2) if min(t1, t2) > 0 else max(t1, t2)

def solve(a, v, l, d, w):
    t = 0.0

    if 2 * a * d <= w * w or v <= w:
        if 2 * a * l <= v * v:
            t = (2 * l / a) ** 0.5
        else:
            t = l / v + v / a / 2
    else:
        tmp = d - 0.5 * v * v / a + 0.5 * (v - w) ** 2 / a - v * (v - w) / a
        if tmp <= 0:
            tmp2 = l - d - (0.5 * (v - w) ** 2 / a + w * (v - w) / a)
            if tmp2 >= 0:
                t = (
                    tmp2 / v
                    + (v - w) / a
                    + 2 * gett(a, 2 * w, w * w / (2 * a) - d)
                    + w / a
                )
            else:
                t = (
                    gett(a / 2, w, d - l)
                    + 2 * gett(a, 2 * w, w * w / (2 * a) - d)
                    + w / a
                )
        else:
            tmp2 = l - d - (0.5 * (v - w) ** 2 / a + w * (v - w) / a)
            if tmp2 >= 0:
                t = (
                    tmp2 / v
                    + (v - w) / a
                    + (2 * v - w) / a
                    + tmp / v
                )
            else:
                t = gett(a / 2, w, d - l) + (2 * v - w) / a + tmp / v
    return t

def generate_test_data(n):
    """
    根据规模 n 生成一组 (a, v, l, d, w) 测试数据。
    n 越大，数值范围越大。
    """
    # 保证 a > 0，其他参数为正整数
    max_val = max(10, n * 10)
    a = random.randint(1, max_val)
    v = random.randint(1, max_val)
    l = random.randint(1, max_val)
    d = random.randint(1, l)  # 典型条件：d 不大于 l
    w = random.randint(1, max_val)
    return a, v, l, d, w

def main(n):
    # 生成测试数据
    a, v, l, d, w = generate_test_data(n)
    # 计算结果
    t = solve(a, v, l, d, w)
    # 输出结果（与原程序格式一致）
    print(f"{t:.12f}")

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)