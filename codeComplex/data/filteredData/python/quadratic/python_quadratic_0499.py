import sys
import threading
import random

sys.setrecursionlimit(2097152)
threading.stack_size(134217728)


def main(n):
    # 1. 生成测试数据：构造一棵 n 个节点的树（0..n-1）
    #   这里随机生成一棵树：
    #   对于每个 i ∈ [1, n-1]，随机选择一个父节点 p ∈ [0, i-1]
    #   原代码中输入是 1-based 父节点，因此这里也先生成 1-based 再减一
    if n == 1:
        # 原逻辑：n==1 时直接输出 1
        print(1)
        return

    # 构造 1-based 父节点数组 a_1based，长度 n-1，表示节点 2..n 的父亲
    parents_1based = [random.randint(1, i) for i in range(1, n)]
    # 转为 0-based，与原逻辑一致
    a = [p - 1 for p in parents_1based]

    vis = [0] * n
    st = [0] * n

    def dfs(g, e):
        if vis[e] == 1:
            return
        vis[e] = 1
        for nxt in g[e]:
            dfs(g, nxt)
        # 叶节点（度为 1）且不是根时计数
        if len(g[e]) == 1 and e != 0:
            st[e] += 1
        for nxt in g[e]:
            st[e] += st[nxt]

    # 建图：无向树
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        u = i + 1
        v = a[i]
        g[u].append(v)
        g[v].append(u)

    dfs(g, 0)
    st.sort()
    print(*st)


# 示例：单独运行本文件时执行一次 main(10)
if __name__ == "__main__":
    t = threading.Thread(target=main, args=(10,))
    t.start()
    t.join()