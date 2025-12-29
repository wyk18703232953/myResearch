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
    random.seed(n)
    # 生成测试数据：
    # a: 加速度 [0.5, 5.0]
    # v: 最大速度 [5.0, 50.0]
    # l: 总路程 [50.0, 500.0]
    # d: 限速路段终点，0 < d < l
    # w: 限速 [1.0, v]
    a = random.uniform(0.5, 5.0)
    v = random.uniform(5.0, 50.0)
    l = random.uniform(50.0, 500.0)
    d = random.uniform(1.0, l - 1.0)
    w = random.uniform(1.0, v)

    if w > v:
        w = v

    x, t = calc(0.0, w, a, d)
    if abs(x - d) < 1e-9:
        ans = go(0.0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2.0 + go(w, v, a, l - d)

    print(ans)

if __name__ == "__main__":
    # 示例：使用 n=1 运行
    main(1)