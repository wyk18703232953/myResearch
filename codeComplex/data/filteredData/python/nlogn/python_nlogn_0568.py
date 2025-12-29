from collections import Counter
import random


def main(n: int):
    # 1. 生成测试数据：构造一棵有 n 个节点的有根树的父节点数组 P（长度 n-1）
    # 保证根为 1，其他节点随机选择一个编号更小的点作为父节点
    if n <= 1:
        # 原程序在 n=1 的情况下不太有意义，这里直接返回
        return

    P = [random.randint(1, i) for i in range(1, n)]  # P[0] 是节点 2 的父亲

    # 2. 原始逻辑

    LIST = [0] * (n + 1)
    LEAF = [1] * (n + 1)

    for p in P:
        LEAF[p] = 0

    for i in range(1, n + 1):
        if LEAF[i] == 1:
            LIST[i] = 1

    for i in range(n, 1, -1):
        LIST[P[i - 2]] += LIST[i]

    counter = Counter(LIST[1:])
    SUM = [0]
    SC = sorted(counter.keys())

    for j in SC:
        SUM.append(SUM[-1] + counter[j])

    i = 1
    j = 0
    out = []
    while j < len(SUM):
        if i <= SUM[j]:
            out.append(str(SC[j - 1]))
        else:
            j += 1
            continue
        i += 1

    print(" ".join(out))


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)