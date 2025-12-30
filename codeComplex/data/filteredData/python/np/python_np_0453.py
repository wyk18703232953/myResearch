import math
import random

def f_local(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 根据规模 n 生成测试数据 (n, x, y)
    # 保证 x, y >= 1 且较为随机
    x = random.randint(1, max(1, n * 2))
    y = random.randint(1, max(1, n * 2))

    g = math.gcd(x, y)

    def h(t):
        return max(f_local(t, 0, x, y + x, g), f_local(t, 1, x, y + x, g))

    yp = y + x  # 对应原代码里的 y += x 后的 y
    # 注意：f_local 内部调用使用的是 g 和 yp，因此 h 内部需要使用 yp
    def h_correct(t):
        return max(f_local(t, 0, x, yp, g), f_local(t, 1, x, yp, g))

    ans = n % g * h_correct(n // g + 1) + (g - n % g) * h_correct(n // g)
    print(ans)

if __name__ == "__main__":
    # 示例调用：规模 n 可自行修改
    main(10)