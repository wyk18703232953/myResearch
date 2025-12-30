import math
import random

def f(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [
            max(d[0], d[1]),
            d[0] + n_val * g // y + (i * x % y < n_val * g % y)
        ]
    return d[s]

def h_func(n_val, x, y, g):
    return max(f(n_val, 0, x, y, g), f(n_val, 1, x, y, g))

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 n 为题目中的 n 上限，x,y 也与 n 同规模
    # 生成范围可根据需要调整
    x = random.randint(1, max(1, n))
    y = random.randint(1, max(1, n))

    g = math.gcd(x, y)
    y_ext = y + x

    q = n // g
    r = n % g

    h_q1 = h_func(q + 1, x, y_ext, g)
    h_q = h_func(q, x, y_ext, g)

    ans = r * h_q1 + (g - r) * h_q
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)