import sys
from collections import Counter
import random

sys.setrecursionlimit(2000)


def build_b_from_a(a):
    """按原逻辑，根据数组 a 生成 b"""
    n = len(a)
    m = n // 2
    b = [0] * m
    for i in range(m):
        b[i] = a[i] + a[n - 1 - i]
    return b


def main(n):
    # 生成测试数据：先随机生成满足条件的 a，然后用原逻辑生成 b
    # 这样再用题目中从 b 还原 a 的算法，可以检验正确性

    if n <= 0:
        return

    random.seed(0)

    # 简单策略：先生成一个非递减的 a[0..n//2-1]，再生成非递增的 a[n//2..n-1]
    half = n // 2
    left = []
    cur = 0
    for _ in range(half):
        cur += random.randint(0, 5)
        left.append(cur)

    right = []
    cur = random.randint(0, 5 * half + 5)
    for _ in range(half):
        cur -= random.randint(0, 5)
        right.append(cur)
    right = right[::-1]  # 从中间往右非增

    a_true = left + right
    b = build_b_from_a(a_true)

    # 原始逻辑：由 b 推出 a
    l = 0
    r = b[0]
    a = [0] * n
    for i in range(n // 2):
        a[i] = l
        a[n - 1 - i] = r
        if i != n // 2 - 1:
            val = b[i + 1]
            summ = l + r
            if summ == val:
                continue
            elif summ > val:
                diff = summ - val
                r -= diff
            else:
                diff = val - summ
                l += diff

    for x in a:
        print(x, end=' ')
    print('')


if __name__ == "__main__":
    # 示例：调用 main(6)
    main(6)