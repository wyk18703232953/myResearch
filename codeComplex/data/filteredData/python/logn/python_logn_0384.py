#!/usr/bin/env python3
import random

def has_intersection(l1, r1, l2, r2):
    if l1 <= l2 and r2 <= r1:
        return True
    if l2 <= l1 and r1 <= r2:
        return True
    return False

def main(n, seed=0):
    """
    n: 偶数，且 n % 4 == 0
    seed: 随机种子，用于生成可重现的测试数据
    """
    random.seed(seed)

    # 生成测试数据 a[0..n-1]
    # 为了保证一定存在解，构造一个 i 使得 a[i] == a[(i + n//2) % n]
    # 其余位置随机。
    assert n >= 2 and n % 2 == 0
    if (n // 2) % 2 == 1:
        # 原逻辑在这种情况下直接输出 -1
        print(-1)
        return

    assert n % 4 == 0

    # 初始化数组
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 构造满足条件的索引 idx
    idx = random.randrange(0, n // 2)
    val = random.randint(0, 10**9)
    a[idx] = val
    a[(idx + n // 2) % n] = val

    # 用原来交互的方式封装 ask(i)
    def ask(i):
        return a[i]

    # ---- 以下为原逻辑的非交互版本 ----
    l1 = 0
    r1 = n // 2
    a_l1 = ask(l1)
    a_r1 = ask(r1)
    if a_l1 == a_r1:
        # 输出满足条件的下标（原程序输出 i+1，这里直接输出下标）
        print(0)
        return

    a_l2 = a_r1
    a_r2 = a_l1

    while True:
        m1 = (l1 + r1) // 2
        m2 = (m1 + n // 2) % n
        a_m1 = ask(m1)
        a_m2 = ask(m2)
        if a_m1 == a_m2:
            print(m1)
            return
        if has_intersection(a_l1, a_m1, a_l2, a_m2):
            r1 = m1
            a_r1 = a_m1
            a_r2 = a_m2
        else:
            assert has_intersection(a_m1, a_r1, a_m2, a_r2)
            l1 = m1
            a_l1 = a_m1
            a_l2 = a_m2

if __name__ == "__main__":
    # 示例：n 必须是 4 的倍数，例如 8, 12, 16, ...
    main(8)