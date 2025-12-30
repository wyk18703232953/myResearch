from random import randint

def construct_tree(n, d, k):
    nodes = []
    edges = []

    if d > n - 1:
        return None

    if k == 1 and n > 2:
        return None

    for i in range(1, d + 2):
        current_deg = k - 1 if i == 1 or i == d + 1 else k - 2
        current_depth = min(i - 1, d - i + 1)
        if current_depth and current_deg:
            nodes.append([i, current_depth, current_deg])
        if i < d + 1:
            edges.append([i, i + 1])

    current_nodes_count = d + 2
    pos = 0
    while current_nodes_count < n + 1:
        if pos >= len(nodes):
            return None

        current = nodes[pos]

        if not current[2]:
            pos += 1
            if pos == len(nodes):
                break
            continue

        if current[1] - 1 and k - 1:
            nodes.append([current_nodes_count, current[1] - 1, k - 1])
        edges.append([current[0], current_nodes_count])
        current[2] -= 1
        current_nodes_count += 1

    if current_nodes_count == n + 1:
        return edges
    return None


def main(n):
    # 简单的测试数据生成策略：
    # 1. 选择 d 在 [1, max(1, n-1)] 范围内
    # 2. 选择 k 在 [1, max(1, n-1)] 范围内
    # 可以根据需要调整策略，使更多情况下可构造出树
    if n < 2:
        d = 0
        k = 1
    else:
        d = randint(1, n - 1)
        k = randint(1, n - 1)

    edges = construct_tree(n, d, k)
    if edges:
        print("YES")
        print('\n'.join(f"{u} {v}" for u, v in edges))
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10) 生成规模为 10 的测试
    main(10)