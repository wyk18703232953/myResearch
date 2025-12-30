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
    # 这里假设 n 代表道路总长度 l 的量级，其它参数按一定规则生成
    # 确保 a > 0, v > 0, l > 0, d 在 [1, l-1]，w > 0
    random.seed(1)

    a = random.randint(1, max(2, n))        # 加速度
    v = random.randint(1, max(2, n * 2))    # 最大速度
    l = random.randint(max(2, n), max(3, n * 3))  # 总路长
    d = random.randint(1, max(1, l - 1))    # 限速区长度起点处的终点
    w = random.randint(1, max(1, v * 2))    # 限速区速度上限

    if w > v:
        w = v

    x, t = calc(0, w, a, d)
    if x == d:
        ans = go(0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)

    print(ans)

if __name__ == "__main__":
    # 示例：用 n = 10 运行一次
    main(10)