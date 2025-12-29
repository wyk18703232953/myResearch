from collections import Counter
import random


def solve_with_array(l, m):
    n = len(l)
    p = l.index(m)
    le, ri = Counter(), Counter()
    c = 0
    le[0] = ri[0] = 1

    # 右边统计
    for i in range(p + 1, n):
        if l[i] < m:
            c += 1
        else:
            c -= 1
        ri[c] += 1

    # 左边统计
    c = 0
    for i in range(p - 1, -1, -1):
        if l[i] < m:
            c -= 1
        else:
            c += 1
        le[c] += 1

    # 统计答案
    res = 0
    for c, x in le.items():
        res += x * (ri[c] + ri[c - 1])
    return res


def main(n):
    """
    n: 规模（数组长度）
    生成测试数据：长度为 n 的数组，包含 1..n 的一个排列，
    选择其中位置 pos 的值为 m，并计算结果。
    """
    if n <= 0:
        return

    # 生成 1..n 的随机排列
    l = list(range(1, n + 1))
    random.shuffle(l)

    # 随机选择一个位置作为 m 的位置
    pos = random.randrange(n)
    m = l[pos]

    # 调用原逻辑
    res = solve_with_array(l, m)

    # 输出测试数据和结果（可根据需要调整输出形式）
    print("n =", n)
    print("array =", l)
    print("m =", m)
    print("answer =", res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)