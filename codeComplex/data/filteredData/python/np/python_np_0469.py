import math
import random

def f_func(n_val, s, x, y, g):
    d = [-n_val, -n_val]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n_val * g // y + (i * x % y < n_val * g % y)]
        # 布尔值在算术中当作 0/1 使用
    return d[s]

def main(n):
    # 根据规模 n 生成测试数据 (n_param, x, y)，保证 x, y > 0
    # 并且适当控制范围，避免极端大数
    max_val = max(1, n)
    n_param = random.randint(1, max_val)
    x = random.randint(1, max_val)
    y = random.randint(1, max_val)

    # 原逻辑开始
    g = math.gcd(x, y)

    def h(t):
        return max(
            f_func(t, 0, x, y, g),
            f_func(t, 1, x, y, g)
        )

    y_ext = y + x  # 对应原代码中的 y += x

    # 注意：f_func 内部使用的是“扩展后”的 y
    # 因此调用时使用 y_ext
    def h_ext(t):
        return max(
            f_func(t, 0, x, y_ext, g),
            f_func(t, 1, x, y_ext, g)
        )

    q, r = divmod(n_param, g)
    ans = r * h_ext(q + 1) + (g - r) * h_ext(q)
    print(ans)

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 规模
    main(1000)