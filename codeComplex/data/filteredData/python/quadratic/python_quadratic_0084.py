import random


def generate_test_graph(n):
    """
    生成测试用有向图：
    - 顶点编号为 1..n
    - 随机生成一定数量的有向边
    """
    # 控制边的密度：大约在 n 到 2n 之间
    m = random.randint(n, max(n, 2 * n))

    digraph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            digraph[u].append(v)

    return digraph


def dfs(graph, u=-1, v=-1):
    n = len(graph)

    pi = [None] * n
    color = ['white'] * n
    for node in range(1, n):
        if color[node] == 'white':
            cicle = dfs_visit(graph, node, color, pi, u, v)
            if cicle is not None:
                return cicle
    return None


def dfs_visit(graph, root, color, pi, u, v):
    stack = [root]

    while stack:
        current_node = stack[-1]

        if color[current_node] != 'white':
            stack.pop()
            color[current_node] = 'black'
            continue

        color[current_node] = 'grey'
        for adj in graph[current_node]:
            if (current_node, adj) == (u, v):
                continue

            if color[adj] == 'white':
                pi[adj] = current_node
                stack.append(adj)
            elif color[adj] == 'grey':
                cicle = [adj]
                while current_node != adj:
                    cicle.append(current_node)
                    current_node = pi[current_node]
                cicle.append(adj)
                return cicle
    return None


def main(n):
    """
    n 为图的规模（顶点数量），根据 n 生成测试数据并执行原逻辑。
    返回值为字符串 "YES" 或 "NO"。
    """
    digraph = generate_test_graph(n)
    cicle = dfs(digraph)
    if cicle is None:
        result = "YES"
    else:
        cicle.reverse()
        for i in range(len(cicle) - 1):
            c = dfs(digraph, cicle[i], cicle[i + 1])
            if c is None:
                result = "YES"
                break
        else:
            result = "NO"
    print(result)
    return result


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(5)