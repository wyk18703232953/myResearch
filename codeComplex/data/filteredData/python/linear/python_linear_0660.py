import random

def main(n):
    # 生成测试数据：
    # 1. 随机生成树的边（n 个节点，n-1 条边）
    # 2. 随机生成 s（题目原逻辑中由输入给出）
    if n <= 1:
        # 对于 n <= 1 的情形，原逻辑中 a.count(1) = 0，会导致除零；
        # 这里直接返回 0.0 作为占位结果。
        print(0.0)
        return

    # 生成随机树：父节点在 [1, i-1] 中随机选择一条边 (parent, i)
    edges = []
    for i in range(2, n + 1):
        parent = random.randint(1, i - 1)
        edges.append((parent, i))

    # 随机生成 s 的值，这里取一个与 n 规模相关的整数
    s = random.randint(1, 10 * n)

    # 以下为原逻辑的实现
    a = [0] * (n + 1)
    for u, v in edges:
        a[u] += 1
        a[v] += 1

    leaf_count = a.count(1)
    if leaf_count == 0:
        # 理论上树中至少有两个叶子，但为了健壮性加一个保护
        print(0.0)
        return

    result = 2.0 * s / leaf_count
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可在此调整
    main(10)