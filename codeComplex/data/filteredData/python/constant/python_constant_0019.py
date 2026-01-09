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
    if n <= 0:
        n = 1

    # 确定性构造输入：
    # a, v, l, d, w 都由 n 通过简单算术确定
    a = n + 1
    v = 2 * n + 3
    l = 5 * n + 10
    d = 3 * n + 4
    w = (n % 7) + 1

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
    main(10)