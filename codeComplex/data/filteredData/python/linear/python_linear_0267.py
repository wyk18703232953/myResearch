import random

def main(n: int):
    # 1. 生成测试数据：构造一棵 n 个节点的树（n-1 条边）
    # 先生成一棵随机树
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 2. 原逻辑开始
    deg = [0] * n

    if n == 2:
        print("Yes")
        print(1)
        print("1 2")
        return

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    ix = deg.index(max(deg))

    if deg[ix] < 3 or deg.count(1) + deg.count(2) == n - 1:
        print("Yes")
        print(deg.count(1))
        for i in range(n):
            if deg[i] == 1:
                print(i + 1, ix + 1)
    else:
        print("No")


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)