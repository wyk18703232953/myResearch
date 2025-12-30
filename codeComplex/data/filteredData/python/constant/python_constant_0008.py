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
    # 根据规模 n 生成测试数据：
    # 将 n 映射到一个合理范围内的加速度和速度/距离
    # 保证均为正数，避免除零与负值问题
    random.seed(n)

    # 生成 a, v
    # a: [1, max(1, n//10 + 1)]
    # v: [1, max(2, n//5 + 2)]
    max_a = max(1, n // 10 + 1)
    max_v = max(2, n // 5 + 2)
    a = random.randint(1, max_a)
    v = random.randint(1, max_v)

    # 生成 l, d, w
    # 路程与限制距离均与 n 相关，使规模随 n 增大
    max_ldw = max(5, n + 5)
    l = random.randint(d_min := 5, max_ldw)          # 总路程
    d = random.randint(1, l)                         # 限速区结束位置，不超过 l
    w = random.randint(1, v)                         # 限速不超过最大速度 v

    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        ans = go(0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)
    print(ans)

if __name__ == "__main__":
    # 示例：以 n = 100 运行
    main(100)