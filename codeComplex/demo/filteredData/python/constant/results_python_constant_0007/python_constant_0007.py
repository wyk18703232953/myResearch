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
    # 确定性生成参数 a, v, l, d, w，规模由 n 控制
    # 使用简单算术关系，保证无随机性
    # 为避免除零，a 至少为 1，v 至少为 1
    a = max(1, n)
    v = max(1, n // 2 + 1)
    l = max(1.0, float(n * 10))
    # d 在 [1, l] 范围内，随 n 增长
    d = float(max(1, n * 5 // 3))
    if d > l:
        d = l * 0.6
    # w 在 [1, v] 范围
    w = float(max(1, v // 3 + n % max(1, v // 5 + 1)))
    if w > v:
        w = float(v)

    a = float(a)
    v = float(v)

    x, t = calc(0.0, w, a, d)
    if x == d:
        result = go(0.0, v, a, l)

    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2.0 + go(w, v, a, l - d)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)