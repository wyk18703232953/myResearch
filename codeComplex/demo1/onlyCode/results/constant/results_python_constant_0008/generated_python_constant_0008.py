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
    # n 控制规模，这里用它来放大距离和速度等参数
    random.seed(42)

    # 加速度 a，最高速 v
    a = random.uniform(1.0, 5.0)
    v = random.uniform(5.0, 20.0)

    # 路程 l，与规模 n 线性相关
    l = random.uniform(10.0 * n, 20.0 * n)

    # 特殊点 d，落在 [0, l] 内
    d = random.uniform(0.0, l)

    # 限速 w，落在 [v/2, 1.5*v] 内
    w = random.uniform(0.5 * v, 1.5 * v)

    if w > v:
        w = v

    x, t = calc(0, w, a, d)
    if abs(x - d) < 1e-9:
        result = go(0, v, a, l)
    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)