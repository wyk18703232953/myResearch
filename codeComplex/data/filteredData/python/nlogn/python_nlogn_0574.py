from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from collections import defaultdict as dd, deque

mod = int(1e9 + 7)


def main(n):
    """
    n 为树的节点数，节点编号为 0..n-1，根为 0。
    这里生成一棵简单的测试树：对于每个 i>=1，父亲为 (i-1)//2（完全二叉树结构）。
    返回原程序最终输出的数组 a（已排序）。
    """

    # 构造父节点数组 P，原程序中 P[i] 是节点 i+1 的父亲（1-based）
    if n <= 0:
        return []

    if n == 1:
        # 原程序中 n==1 时输出 [1]
        a = [1]
        print(*a)
        return a

    # 生成一棵完全二叉树作为测试数据
    # 对于 i in [1..n-1]，父亲为 (i-1)//2
    P = [((i - 1) // 2) + 1 for i in range(1, n)]  # 转成 1-based，长度 n-1

    # 原程序逻辑开始
    tree = [{} for _ in range(n)]
    if n > 1:
        for i in range(n - 1):
            tree[P[i] - 1][i + 1] = 0
        a = [0] * n
        for i in range(n - 1, -1, -1):
            if len(tree[i]) == 0:
                a[i] = 1
            else:
                for j in tree[i]:
                    a[i] += a[j]
        a.sort()
    else:
        a = [1]

    print(*a)
    return a


if __name__ == "__main__":
    # 示例：调用 main(7) 生成规模为 7 的测试数据并运行
    main(7)