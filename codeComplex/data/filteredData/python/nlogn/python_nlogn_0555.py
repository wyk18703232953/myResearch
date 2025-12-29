MOD = 10**9 + 7
from collections import defaultdict
import random

def generate_tree_and_bfs_order(n, seed=0):
    """
    生成一棵随机树和它的一个 BFS 序列（从根 1 开始）。
    返回: (edges, bfs_order)
    edges: list[(u, v)]
    bfs_order: list[int]，长度为 n
    """
    random.seed(seed)

    # 1. 生成一棵随机树（1..n），用随机父亲构造
    parent = [0] * (n + 1)
    for i in range(2, n + 1):
        parent[i] = random.randint(1, i - 1)

    edges = []
    for i in range(2, n + 1):
        edges.append((parent[i], i))

    # 2. 构建邻接表
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    # 3. 按 BFS 生成 l（访问相邻结点的顺序打乱以保证随机性）
    for u in g:
        random.shuffle(g[u])

    bfs_order = []
    from collections import deque
    q = deque([1])
    vis = [False] * (n + 1)
    vis[1] = True

    while q:
        u = q.popleft()
        bfs_order.append(u)
        for v in g[u]:
            if not vis[v]:
                vis[v] = True
                q.append(v)

    return edges, bfs_order


def main(n):
    """
    规模 n 的主逻辑：
    1. 随机生成一棵 n 结点的树及其 BFS 序列 l。
    2. 在不使用 input() 的情况下运行原先的校验逻辑。
    3. 输出 "Yes" 或 "No"，并返回同样的字符串。
    """
    # 生成测试数据
    edges, l = generate_tree_and_bfs_order(n)

    # 建图
    d = defaultdict(list)
    for u, v in edges:
        d[u].append(v)
        d[v].append(u)

    # 原始逻辑开始
    v = [0] * (n + 1)
    s = 1
    what = 0
    v[1] = 1

    # l 作为“队列”式访问顺序
    while what < s:
        a = set()
        i = l[what]
        for j in d[i]:
            if not v[j]:
                a.add(j)

        b = set()
        for j in range(s, s + len(a)):
            if j >= len(l):
                # 越界则必然不匹配
                print('No')
                return 'No'
            b.add(l[j])

        if a != b:
            print('No')
            return 'No'

        kkk = 0
        for k in a:
            kkk += 1
            v[k] = 1
        s += kkk
        what += 1

    if s != n:
        print('No')
        return 'No'

    print('Yes')
    return 'Yes'


if __name__ == "__main__":
    # 示例运行：规模 n=10
    main(10)