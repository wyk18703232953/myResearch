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
    """
    n 用于控制测试数据规模。
    返回值为原程序本应输出的时间浮点数。
    """
    # 根据 n 生成测试数据（只是一个示例策略，可按需调整）
    # 保证加速度与速度为正数，距离非负。
    a = max(1.0, float(n))                    # 加速度
    v = max(1.0, float(n) * 2.0)              # 最大速度
    l = max(10.0, float(n) * 10.0)            # 总路程
    d = max(0.0, min(l * 0.5, float(n) * 5))  # 限速路段长度
    w = max(1.0, min(v, float(n) * 1.5))      # 限速

    if w > v:
        w = v

    x, t = calc(0, w, a, d)
    if x == d:
        result = go(0, v, a, l)
    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    print(result)
    return result

if __name__ == "__main__":
    # 示例调用：以 n=10 作为规模参数
    main(10)