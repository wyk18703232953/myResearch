from collections import defaultdict
import random


def solve_tree(connections, n, k):
    leafs = set()
    for node in connections:
        if len(connections[node]) == 1:
            leafs.add(node)

    steps = 0
    is_correct = True
    while is_correct and steps <= k:
        new_leafs = set()
        for x in leafs:
            if len(connections[x]) > 1:
                is_correct = False
                break
            root = list(connections[x])[0]
            if len(connections[root]) < 4 and len(leafs) != 3:
                is_correct = False
                break
        if not is_correct:
            break
        for x in leafs:
            root = list(connections[x])[0]
            new_leafs.add(root)
            connections[root].remove(x)
        leafs = new_leafs
        steps += 1
        if len(leafs) == 1 and len(connections[list(leafs)[0]]) == 0:
            break

    return "Yes" if is_correct and steps == k else "No"


def generate_tree(n):
    """
    生成一棵随机树（n 个节点，节点编号 1..n）
    使用随机父节点生成一棵树。
    """
    connections = defaultdict(set)
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        connections[u].add(v)
        connections[v].add(u)
    # 确保所有节点都在字典里
    for i in range(1, n + 1):
        if i not in connections:
            connections[i] = set()
    return connections


def main(n):
    """
    n: 树的规模 (节点数)
    自动生成一棵规模为 n 的树，并选择一个 k 来运行原逻辑。
    """
    if n < 2:
        # 原程序逻辑基于一棵有 n-1 条边的树，n>=2 更合理
        n = 2

    # 生成测试数据：树
    connections = generate_tree(n)

    # 生成 k：可根据需要调整策略，这里取 [0, n] 内的随机值
    k = random.randint(0, n)

    # 运行原逻辑
    ans = solve_tree(connections, n, k)

    # 输出结果（与原程序一致，仅打印 Yes/No）
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，给定规模 n
    main(10)