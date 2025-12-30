from math import sqrt
import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # n 越大，生成的数据范围越大，仅作示例，可根据需要调整规则
    random.seed(n)

    # a 为加速度，v 为最大速度
    # l 为总路程，d 为限速路段长度，w 为限速
    # 保证基本物理量为正，并构造一个相对合理的范围
    a = random.randint(1, 5 + n)          # 1 ~ (5 + n)
    v = random.randint(1, 20 + 2 * n)     # 1 ~ (20 + 2n)
    l = random.randint(1, 100 + 10 * n)   # 1 ~ (100 + 10n)
    d = random.randint(1, max(1, l - 1))  # 1 ~ l-1，保证 d < l
    w = random.randint(1, v)              # 限速不超过最大速度

    # 原逻辑开始
    w = min(v, w)
    lowtime = (v - w) / a
    lowdist = v * lowtime - a * lowtime**2 / 2
    startdist = v**2 / (2 * a)

    if startdist + lowdist <= d:
        ans = v / a + (d - startdist - lowdist) / v + lowtime
    elif w**2 <= 2 * d * a:
        u = sqrt(a * d + w**2 / 2)
        ans = (2 * u - w) / a
    else:
        ans = sqrt(2 * d / a)
        w = ans * a

    hightime = (v - w) / a
    highdist = w * hightime + a * hightime**2 / 2

    if highdist <= l - d:
        ans += hightime + (l - d - highdist) / v
    else:
        disc = sqrt(w**2 + 2 * a * (l - d))
        ans += (disc - w) / a

    print(f'{ans:.7f}')


# 示例：若需要运行，可调用
# main(10)