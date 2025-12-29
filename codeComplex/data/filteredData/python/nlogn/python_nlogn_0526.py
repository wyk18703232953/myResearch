import sys
from collections import defaultdict
import random


def solve_one_case(lengths):
    out = sys.stdout
    dic = defaultdict(int)
    ls = sorted(lengths, reverse=True)
    st = set()

    # 检查是否存在四条相同边
    for x in ls:
        dic[x] += 1
        if dic[x] == 4:
            out.write(f"{x} {x} {x} {x}\n")
            return

    # 找所有出现次数至少为2的边长
    for x in ls:
        if dic[x] >= 2:
            st.add(x)

    st = sorted(st, reverse=True)
    ln = len(st)

    # 至少要两种边长才能组成矩形
    if ln < 2:
        # 若无法组成矩形，简单输出四个相同的最小边（退化情形）
        x = st[0] if ln == 1 else ls[-1]
        out.write(f"{x} {x} {x} {x}\n")
        return

    # 选取使得 (4*(a+b)^2)/(ab) 最小的相邻两种边长
    mn = (4 * (st[0] + st[1]) ** 2) / (st[0] * st[1])
    a, b, c, d = st[1], st[1], st[0], st[0]

    for i in range(1, ln - 1):
        val = (4 * (st[i] + st[i + 1]) ** 2) / (st[i] * st[i + 1])
        if val < mn:
            mn = val
            a, b, c, d = st[i], st[i], st[i + 1], st[i + 1]

    out.write(f"{a} {b} {c} {d}\n")


def main(n: int):
    """
    n: 规模参数，用来生成测试数据。
       这里约定：
       - 测试组数 t = max(1, n // 5)
       - 每组长度数量 m = max(4, n)
       - 边长值在 [1, 1000] 中随机生成
    """
    random.seed(0)
    t = max(1, n // 5)
    for _ in range(t):
        m = max(4, n)
        # 生成一组数据：m 个随机边长
        lengths = [random.randint(1, 1000) for _ in range(m)]
        solve_one_case(lengths)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)