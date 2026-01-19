import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 将 n 映射为原程序中的 n, x, y，保持确定性
    # 约束：x, y > 0，且 gcd(x, y) 在可控范围
    N = max(1, n)
    x = N + 1
    y = 2 * N + 1

    g = math.gcd(x, y)
    h = lambda t: max(f(t, 0, x, y, g), f(t, 1, x, y, g))
    yy = y + x
    # 原代码中 y 被修改为 y += x，这里直接用 yy
    # 后续使用的 g 仍为 gcd(x, y)（与原逻辑保持一致）
    # 注意 f 内部需要使用修改后的 y，这里传入 yy
    g2 = math.gcd(x, yy)
    h2 = lambda t: max(f(t, 0, x, yy, g2), f(t, 1, x, yy, g2))

    return N % g2 * h2(N // g2 + 1) + (g2 - N % g2) * h2(N // g2)

if __name__ == "__main__":
    # 示例调用
    for n in range(1, 6):
        print(n, main(n))