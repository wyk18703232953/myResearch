import math

def f(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    # 确定性生成 x, y：保证与 n 有关且规模可控
    # 约束：y 初始值需为 g 的倍数，否则与原逻辑一致性受 gcd 影响不大
    x = n + 1
    y = 2 * n + 3  # y > x 以保证循环次数随 n 增长
    g = math.gcd(x, y)
    h = lambda t: max(f(t, 0, x, y + x, g), f(t, 1, x, y + x, g))
    yy = y + x  # 对应原代码中的 y += x 后的值
    # 重新计算 g 针对 x, yy 的 gcd，与原逻辑保持一致
    g = math.gcd(x, yy)
    result = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(result)

if __name__ == "__main__":
    main(10)