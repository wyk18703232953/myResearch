def f(n, s, y, g, x):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def solve_one(n, x, y):
    import math
    g = math.gcd(x, y)
    h = lambda k: max(f(k, 0, y + x, g, x), f(k, 1, y + x, g, x))
    y2 = y + x
    return n % g * h(n // g + 1) + (g - n % g) * h(n // g)

def main(n):
    # 解释 n 的含义：
    # 我们构造 n 组测试数据，第 i 组的 (n_i, x_i, y_i) 确定性生成，
    # 并对每组调用一次原始逻辑，用于规模化的时间复杂度实验。
    if n <= 0:
        return

    results = []
    for i in range(1, n + 1):
        # 确定性构造输入：
        # 原程序需要三个正整数 n, x, y
        # 保证 x, y > 0 且有一定变化
        ni = i * 10
        xi = 2 * i + 1
        yi = 3 * i + 2
        results.append(solve_one(ni, xi, yi))

    # 为防止 Python 优化掉计算，这里汇总输出一个确定性结果
    total = 0
    for v in results:
        total ^= v
    print(total)

if __name__ == "__main__":
    main(1000)