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
    random.seed(n)
    # 简单策略：a, v, l, d, w 随着 n 线性增长，保证有意义的正数
    a = random.randint(1, max(2, n))
    v = random.randint(1, max(2, n * 2))
    l = random.randint(1, max(2, n * 10))
    d = random.randint(1, max(1, l))  # d 不超过 l
    w = random.randint(1, max(2, v * 2))

    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        result = go(0, v, a, l)
    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)
    print(result)

if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)