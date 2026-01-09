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

    # 将 n 映射为原程序的输入参数：
    # a, v, l, d, w 全部由 n 以确定性方式构造
    # 这里选择：
    # a = (n % 5) + 1         (加速度 1~5)
    # v = (n % 50) + 10       (最大速度 10~59)
    # l = 10 * n              (总路程与规模线性相关)
    # d = max(1, min(l - 1, 3 * n))  (减速区终点，处于 [1, l-1])
    # w = (n % v) + 1         (减速区限速，不超过 v)
    a = (n % 5) + 1
    v = (n % 50) + 10
    l = 10 * n
    d = 3 * n
    if d >= l:
        d = l - 1
    if d <= 0:
        d = 1
    w = (n % v) + 1

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