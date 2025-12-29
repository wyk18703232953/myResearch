import random
import math

def gett(a, b, c):
    delta = b ** 2 - 4 * a * c
    t1 = (-b + delta ** 0.5) / (2 * a)
    t2 = (-b - delta ** 0.5) / (2 * a)
    if min(t1, t2) > 0:
        return min(t1, t2)
    else:
        return max(t1, t2)

def main(n):
    # 根据 n 生成一组测试数据 (a, v, l, d, w)
    # 仅做示例：n 影响数值范围
    # 保证 a > 0，其他为非负数
    random.seed(n)
    a = random.randint(1, max(1, n))
    v = random.randint(1, max(1, 2 * n))
    l = random.randint(1, max(1, 3 * n))
    d = random.randint(0, max(0, l))          # d 不超过 l，保持场景合理
    w = random.randint(0, max(1, v))          # w 不超过 v

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
                t = tmp2 / v + (v - w) / a + 2 * gett(a, 2 * w, w * w / (2 * a) - d) + w / a
            else:
                t = gett(a / 2, w, d - l) + 2 * gett(a, 2 * w, w * w / (2 * a) - d) + w / a
        else:
            tmp2 = l - d - (0.5 * (v - w) ** 2 / a + w * (v - w) / a)
            if tmp2 >= 0:
                t = tmp2 / v + (v - w) / a + (2 * v - w) / a + tmp / v
            else:
                t = gett(a / 2, w, d - l) + (2 * v - w) / a + tmp / v

    print(f"{t:.12f}")
    return t

# 示例调用
if __name__ == "__main__":
    main(10)