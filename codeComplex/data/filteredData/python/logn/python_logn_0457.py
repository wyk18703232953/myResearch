import random
import sys


# 全局真实数 a, b 以及当前构造的 c, d
a = 0
b = 0
c = 0
d = 0


def ask(x, y):
    """
    原题中的交互函数：返回 sign((a ^ x) - (b ^ y))
    这里用本地的 a, b 模拟。
    返回值：
        -1 : (a ^ x) < (b ^ y)
         0 : (a ^ x) == (b ^ y)
         1 : (a ^ x) > (b ^ y)
    在原题中似乎只会返回 -1 或 1，这里保留 0 以防万一。
    """
    ax = a ^ x
    by = b ^ y
    if ax < by:
        return -1
    elif ax > by:
        return 1
    else:
        return 0


def solve(mi, base):
    def solve_same():
        global c, d
        for i in range(mi, -1, -1):
            bit = 1 << i
            res1 = ask(c ^ bit, d)
            res2 = ask(c, d ^ bit)
            if res1 == -1 and res2 == 1:
                c |= bit
                d |= bit

    def solve1():
        global c, d
        for i in range(mi, -1, -1):
            bit = 1 << i
            res1 = ask(c ^ bit, d ^ bit)
            if res1 == -1:
                # a[i] == 1, b[i] == 0
                c |= bit
                return solve(i - 1, ask(c, d))
            else:
                # a[i] == b[i]
                res2 = ask(c ^ bit, d)
                if res2 == -1:
                    # a[i] == b[i] == 1
                    c |= bit
                    d |= bit

    def solve2():
        global c, d
        for i in range(mi, -1, -1):
            bit = 1 << i
            res1 = ask(c ^ bit, d ^ bit)
            if res1 == 1:
                # a[i] == 0, b[i] == 1
                d |= bit
                return solve(i - 1, ask(c, d))
            else:
                # a[i] == b[i]
                res2 = ask(c, d ^ bit)
                if res2 == 1:
                    # a[i] == b[i] == 1
                    c |= bit
                    d |= bit

    if base == 0:
        solve_same()
    elif base == 1:
        solve1()
    else:
        solve2()


def main(n):
    """
    n 为规模：以 n 位二进制为上限随机生成 a, b（0 <= a, b < 2^n）。
    执行原算法恢复 c, d，并打印结果及验证信息。
    """
    global a, b, c, d

    # 生成测试数据：n 位以内的随机整数
    if n <= 0:
        max_val = 1
    else:
        max_val = 1 << n

    a = random.randrange(0, max_val)
    b = random.randrange(0, max_val)

    c = 0
    d = 0

    # 使用最高位索引 mi = n-1（至少为 0）
    mi = max(0, n - 1)
    solve(mi, ask(0, 0))

    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("(a ^ c) =", a ^ c)
    print("(b ^ d) =", b ^ d)
    print("equal:", (a ^ c) == (b ^ d))


if __name__ == "__main__":
    # 示例：n = 30
    main(30)