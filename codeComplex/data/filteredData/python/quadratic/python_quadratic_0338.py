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
    # 映射规则：
    # n -> 输入规模
    #   原程序输入为三个整数 n, d, k
    #   这里使用 n 作为原始节点数量
    #   d 和 k 作为确定性的函数：
    #       d = max(1, n // 3)
    #       k = max(2, min(10, n // 2))
    nodes_count = max(1, n)
    d = max(1, nodes_count // 3)
    k = max(2, min(10, nodes_count // 2))

    edges = construct_tree(nodes_count, d, k)
    if edges:
        print('YES')
        print('\n'.join(['{0} {1}'.format(e[0], e[1]) for e in edges]))
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值进行规模化实验
    main(10)