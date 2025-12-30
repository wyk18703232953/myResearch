from collections import deque
import random

mod = 10**9 + 7
INF = float('inf')


def main(n: int):
    # 1. 生成一棵规模为 n 的随机树
    # 节点编号为 0..n-1
    edges = [[] for _ in range(n)]
    for v in range(1, n):
        # 随机连接到前面任意一个节点，保证是树
        u = random.randint(0, v - 1)
        edges[u].append(v)
        edges[v].append(u)

    # 2. 原逻辑开始
    dist = [-1] * n
    dist[0] = 0
    pa = [-1] * n
    se = set()
    pq = []
    q = deque()
    q.append(0)

    while q:
        now = q.popleft()
        for nx in edges[now]:
            if dist[nx] != -1:
                continue
            pa[nx] = now
            dist[nx] = dist[now] + 1
            if dist[nx] > 2:
                se.add(nx)
                pq.append((dist[nx], nx))
            q.append(nx)

    pq = pq[::-1]
    res = 0
    ind = 0

    while se:
        d, v = pq[ind]
        ind += 1
        if v not in se:
            continue
        res += 1
        pv = pa[v]
        se.discard(pv)
        for nv in edges[pv]:
            se.discard(nv)

    print(res)


if __name__ == "__main__":
    # 示例：运行规模为 10 的随机树
    main(10)