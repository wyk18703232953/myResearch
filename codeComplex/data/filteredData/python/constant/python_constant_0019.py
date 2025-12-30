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
    # 依据规模 n 生成测试数据
    # n 控制数据的大致量级
    random.seed(0)
    # 确保 a>0, l>0, d>0, v>=1, w>=1
    a = random.randint(1, max(2, n))
    v = random.randint(1, max(2, n))
    l = random.randint(1, max(10, n * 10))
    d = random.randint(1, max(10, n * 10))
    w = random.randint(1, max(2, v))

    if w > v:
        w = v

    x, t = calc(0, w, a, d)
    if x == d:
        ans = go(0, v, a, l)
    else:
        ans = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)
    print(ans)

if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)