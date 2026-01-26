import math

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
    # 确定性生成参数：
    # a, v 控制加速度和最大速度
    # l, d, w 控制赛道总长、限速区间长度和限速值
    # 使用简单算术表达式构造，确保可规模化和确定性
    a = max(1, n // 10 + 1)          # 加速度，随 n 缓慢增大
    v = max(1, n // 5 + 2)           # 最高速度，随 n 增大
    l = max(1, n * 10)               # 总长度，线性随 n 增大
    d = max(1, min(l // 2, n * 3))   # 限速区长度，不超过总长度一半
    w = max(1, (n % 7) + v // 2)     # 限速值，相对 v 做简单偏移

    if w > v:
        w = v

    x, t = calc(0, w, a, d)
    if x == d:
        result = go(0, v, a, l)

    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    # print(result)
    pass
if __name__ == "__main__":
    main(1000)