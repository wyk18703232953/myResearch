import collections

def main(n):
    if n < 2:
        n = 2

    N = n
    # 构造一个确定性的父节点数组 p，表示节点 2..N 的父节点
    # 这里使用 i//2 的方式构造一棵接近完全二叉树
    p = [i // 2 for i in range(1, N)]

    G = collections.defaultdict(list)

    for i, v in enumerate(p):
        u = i + 2
        G[u].append(v)
        G[v].append(u)

    root = 1

    colors = [0] * (N + 1)
    counts = [0] * (N + 1)

    q = [root]
    parents = [0] * (N + 1)
    vis = [0] * (N + 1)
    while q:
        u = q.pop()
        if vis[u]:
            colors[parents[u]] += colors[u]
            continue
        children = [v for v in G[u] if v != parents[u]]
        for v in children:
            parents[v] = u

        if children:
            vis[u] = True
            q.append(u)
            q.extend(children)
        else:
            vis[u] = True
            colors[u] = 1
            colors[parents[u]] += 1

    colors = colors[1:]
    colors.sort()
    print(' '.join(map(str, colors)))


if __name__ == "__main__":
    main(10)