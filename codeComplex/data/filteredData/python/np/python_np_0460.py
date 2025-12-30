import math

def f_func(n, s, x, y, g):
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]),
             d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def h_func(N, x, y, g):
    return max(f_func(N, 0, x, y, g), f_func(N, 1, x, y, g))

def main(n):
    # 根据规模 n 生成测试数据，这里示例设定 x, y 与 n 同数量级
    # 可按需要修改生成策略
    x = n + 1
    y = n + 2

    g = math.gcd(x, y)
    h = lambda N: h_func(N, x, y + x, g)  # 注意原始代码中后续使用的是更新后的 y

    # 原代码中 y 在读入后被更新为 y + x
    y_updated = y + x

    # 重新计算 g，因为在原始逻辑中 gcd 是基于初始 x, y 计算的
    # 但 f 和 h 中使用的 y 是更新后的 y + x，g 仍使用原来的 gcd(x, y)
    # 保持与原代码逻辑一致
    # g 已经是基于原始 x, y 的 gcd

    # 计算结果
    result = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(result)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)