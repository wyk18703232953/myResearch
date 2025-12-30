#!/usr/bin/env python
import random

def main(n):
    """
    n: 规模，用于生成测试数据
    逻辑与原程序一致：
    给定 n, k 以及长度为 n 的数组 l，统计满足条件的不同元素个数：
    遍历排序后的 l，若 l[i] 不在 d 中，则计入集合 c，并在 d 中标记 l[i] * k。
    返回 len(c)。
    """

    # 根据 n 生成测试数据
    # 可以按需修改生成策略
    k = random.randint(2, 10)              # 生成一个 k（原题中为输入）
    max_val = max(2 * n, 10)
    l = [random.randint(1, max_val) for _ in range(n)]

    # 原逻辑开始
    d = dict()
    c = set()
    l.sort()
    for i in range(n):
        if not d.get(l[i]):
            c.add(l[i])
            d.setdefault(l[i] * k, 1)

    # 输出结果（或返回结果，根据需要）
    print(len(c))
    return len(c)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)