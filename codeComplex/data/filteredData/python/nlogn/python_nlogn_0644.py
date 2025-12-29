from bisect import bisect_right as br
from bisect import bisect_left as bl
import random

MAX = 10**9

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)

def main(n):
    # 生成测试数据
    # n 保持为原程序中的 n（v 的长度）
    # m 按规模设定，例如 m = 2 * n + 5（至少为 1）
    if n < 0:
        n = 0
    m = max(1, 2 * n + 5)

    # 生成 v：n 个 1..MAX-1 的整数
    v = [random.randint(1, MAX - 1) for _ in range(n)]

    # 生成水平线段输入 (x1, x2, y)
    # 保证至少部分有 x1==1
    h = []
    for i in range(m):
        if i % 2 == 0:
            x1 = 1
        else:
            x1 = random.randint(1, 5)
        x2 = random.randint(1, MAX)
        y = random.randint(1, MAX)
        if x1 == 1:
            h.append(x2)

    lh = len(h)
    h.sort()
    v.sort()

    if not lh:
        result = 0
    elif n == 0:
        result = lh - bl(h, MAX)
    else:
        mn = n + lh - bl(h, MAX)
        for i in range(n):
            mn = min(mn, lh - bl(h, v[i]) + i)
        result = mn

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(10)