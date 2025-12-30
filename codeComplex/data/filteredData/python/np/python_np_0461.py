import math
import random

def f(n, s, x, y, g):
    # 原代码的 f(n, s) ，增加 x, y, g 作为参数
    d = [-n, -n]
    d[s] = 0
    for i in range(y // g):
        d = [max(d[0], d[1]), d[0] + n * g // y + (i * x % y < n * g % y)]
    return d[s]

def main(n):
    """
    n 为规模参数，用于生成测试数据并执行原逻辑。
    这里根据 n 生成 x, y：
      1 <= x, y <= n（并保证 gcd(x, y) > 0）
    """
    if n < 1:
        raise ValueError("n 必须为正整数")

    # 简单的基于 n 的测试数据生成策略：
    # 确保 x, y 在 [1, n] 范围内，避免为 0
    random.seed(1)  # 固定随机种子，保证可复现
    x = random.randint(1, n)
    y = random.randint(1, n)

    g = math.gcd(x, y)
    # 防御性处理：如果 gcd 为 0（理论上不会，因为 x,y>=1），则修正
    if g == 0:
        g = 1

    # h 函数依赖当前的 x, y, g
    def h(k):
        return max(f(k, 0, x, y, g), f(k, 1, x, y, g))

    yy = y + x  # 对应原代码的 y = y + x
    # 注意：上面已经使用 y 参与计算 g 和 h 定义；此处仅按原逻辑修改 y 的值
    # 为保持与原代码一致，下方使用 yy 代替原来的 y 变量
    # 但 f 中的循环长度由传入的 y//g 决定，所以需用 yy 作为 y 参与 f
    # 故在真正调用 h 时，需要让 f 使用更新后的 y（即 yy）
    # 为此，重新定义 h，使其使用新的 y 值
    def h(k):
        return max(f(k, 0, x, yy, g), f(k, 1, x, yy, g))

    # 按原表达式计算结果
    res = n % g * h(n // g + 1) + (g - n % g) * h(n // g)
    print(res)

if __name__ == "__main__":
    # 示例：用一个规模参数运行
    main(10)