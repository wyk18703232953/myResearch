import math
import random

def calc(v0, v, a, x):
    t = (v - v0) / a
    x0 = v0 * t + 0.5 * a * t * t
    if x0 >= x:
        return (x, (math.sqrt(v0 * v0 + 2 * a * x) - v0) / a)
    return (x0, t)

def go(v0, v, a, x):
    x0, t = calc(v0, v, a, x)
    return t + (x - x0) / v

def main(n):
    # 根据规模 n 生成测试数据
    # 这里简单设定：
    # a = 1 ~ n
    # v = 1 ~ n
    # l = 1 ~ n
    # d = 1 ~ l
    # w = 1 ~ v
    if n < 1:
        n = 1
    random.seed(n)
    a = random.randint(1, n)
    v = random.randint(1, n)
    l = random.randint(1, n)
    d = random.randint(1, l)
    w = random.randint(1, max(1, v))

    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        ans = go(0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    print(ans)
    return ans