from collections import deque
import random

def main(n):
    # n 作为树的节点个数，这里对应原程序中的 m
    m = n

    # 生成一棵随机树（m 个点）
    # 先生成一棵连通无环图（树）：随机把每个节点 2..m 连接到 [1, i-1] 中的一个节点
    edges = []
    for v in range(2, m + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))

    # 为了让逻辑有机会输出 Yes，随机生成一个 k（步数要求）
    # 合理范围：[0, m]，也可以根据需要调整
    k = random.randint(0, m)

    # ============ 以下是原逻辑的封装，去掉 input() ============

    G = [set() for _ in range(m + 1)]
    q, nq = deque(), deque()

    # 建图
    for u, v in edges:
        G[u].add(v)
        G[v].add(u)

    # 初始叶子入队
    for u in range(1, m + 1):
        if len(G[u]) == 1:
            q.append(u)

    step = 0
    removed = 0
    ok = True

    # 分层剥离叶子
    while removed < m - 1:
        each = {}
        for u in q:
            nxt = G[u].pop()
            G[nxt].remove(u)
            each[nxt] = each.get(nxt, 0) + 1
            removed += 1
            if len(G[nxt]) == 0:
                break
            if len(G[nxt]) == 1:
                nq.append(nxt)
        if any(v < 3 for v in each.values()):
            ok = False
            break
        q, nq = nq, deque()
        step += 1

    if ok and step == k and removed == m - 1:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)