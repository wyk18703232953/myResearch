from collections import Counter
import random

def main(n: int):
    # 生成测试数据
    # 约定：生成一个 n 个节点的树，节点编号为 1..n
    # 随机生成边，保证为树
    if n < 2:
        # 原逻辑中 n-1 条边，n 至少为 2 才有意义
        return

    # 随机生成一个连通无环图（树）
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 随机生成 s（原程序中是从输入读取的第二个整数）
    # 根据原题意通常 s 为整数，这里给定一个合适的正整数范围
    s = random.randint(1, 10**6)

    # 以下为原逻辑实现
    d = Counter()
    for u, v in edges:
        d[u] += 1
        d[v] += 1

    # 叶子节点个数
    l = sum(deg == 1 for deg in d.values())
    ans = s / l * 2
    print('%.10f' % ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)