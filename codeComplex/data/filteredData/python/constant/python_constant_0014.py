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
    # a, v, l, d, w 都与 n 线性相关，保证正数且有一定变化
    a = max(1, n)          # 加速度
    v = max(1, 2 * n)      # 最大速度
    l = max(1, 10 * n)     # 总路程
    d = max(1, 3 * n)      # 限速区间长度
    w = max(1, n)          # 限速

    # 可根据需要随机微调
    # 确保 d 不大于 l
    if d > l:
        d = l // 2 or 1

    # 按原逻辑处理
    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        ans = go(0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    print(ans)

if __name__ == "__main__":
    # 示例运行：传入某个规模 n
    main(10)