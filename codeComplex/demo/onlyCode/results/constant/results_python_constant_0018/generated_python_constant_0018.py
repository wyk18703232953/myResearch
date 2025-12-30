import math
import random

def calc(v0, v, a, x):
    # 从速度 v0 以加速度 a 加速到 v，运动位移 x，返回到达 x 的最早时刻
    t = (v - v0) / a
    x0 = v0 * t + 0.5 * a * t * t
    if x0 >= x:
        # 在加速过程中已经到达 x
        return (x, (math.sqrt(v0 * v0 + 2 * a * x) - v0) / a)
    # 先加速到 v，再匀速走到 x
    return (x0, t)

def go(v0, v, a, x):
    # 从 v0 加速到 v（若需要），再以 v 匀速跑完总长 x 所需时间
    x0, t = calc(v0, v, a, x)
    return t + (x - x0) / v

def main(n):
    """
    n 为规模参数，这里简单用来控制随机测试数据的范围:
      a: 1 ~ n
      v: 1 ~ n
      l: 1 ~ 10n
      d: 0 ~ l
      w: 0 ~ v + n
    返回值与原程序输出一致：单个 float 时间值。
    """
    if n <= 0:
        n = 1

    # 生成测试数据
    a = random.randint(1, n)
    v = random.randint(1, n)
    l = random.randint(1, 10 * n)
    d = random.randint(0, l)
    w = random.randint(0, v + n)

    # 与原逻辑一致
    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        return go(0, v, a, l)
    else:
        return t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

# 示例: 如需直接运行并查看一个结果，可取消下面的注释
# if __name__ == "__main__":
#     print(main(10))