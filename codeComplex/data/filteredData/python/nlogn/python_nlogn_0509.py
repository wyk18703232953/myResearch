import random
from collections import Counter

def main(n):
    """
    n: 问题规模，这里作为数组长度使用。
    逻辑等价于原程序中单个测试用例的处理。
    测试数据自动生成：
      - 随机生成长度为 n 的数组 a，元素为 1..max(4, n//2)
      - 试图保证存在至少两种数出现次数 >=2，以保证有解的概率
    """

    # ---------- 生成测试数据 ----------
    # 原逻辑：读取 tc, 然后每个用例读 n 和数组 a
    # 这里仅做一个用例，规模为 n
    max_val = max(4, n // 2)
    a = [random.randint(1, max_val) for _ in range(n)]

    # 调整一下，尽量制造多一些重复元素，使结果更稳定
    if n >= 4:
        v1 = random.randint(1, max_val)
        v2 = random.randint(1, max_val)
        # 保证 v1 出现至少两次
        a[0] = v1
        a[1] = v1
        # 保证 v2 出现至少两次（可能和 v1 相同，也没关系）
        if n >= 4:
            a[2] = v2
            a[3] = v2

    # ---------- 原核心逻辑（单个 test case） ----------
    d = Counter(a)
    distinct = sorted(list(set(a)))
    cand = []
    picked_four = False

    # 如果有某个数出现次数 >= 4，直接输出 x x x x
    for x in distinct:
        if d[x] >= 4:
            picked_four = True
            print(x, x, x, x)
            break
        if d[x] >= 2:
            cand.append(x)

    # 否则在出现次数>=2的数中找最优比例
    if not picked_four:
        # 选出 (lx, lx, bx, bx) 使得 lx/bx 最小
        # 即比较 l*bx < lx*b
        if len(cand) < 2:
            # 如果候选不足两个，就退化输出任意 4 个相同的数（保证输出）
            x = distinct[0]
            print(x, x, x, x)
            return

        lx = 10**40
        bx = 1
        for i in range(len(cand) - 1):
            b = cand[i]
            l = cand[i + 1]
            if l * bx < lx * b:
                lx, bx = l, b
        print(lx, lx, bx, bx)


if __name__ == "__main__":
    # 示例：运行一个规模为 10 的用例
    main(10)