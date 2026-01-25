import sys
import threading

sys.setrecursionlimit(2097152)
threading.stack_size(134217728)

def main(n):
    # 构造确定性的父节点数组 a，原始代码中读入的第二行
    # 这里让 a[i] = i // 2 + (i % 3 == 0) 再对 n 取模，保证是合法父节点且结构可规模化
    if n <= 0:
        return
    if n == 1:
        print(1)
        return

    a = [((i // 2) + (1 if i % 3 == 0 else 0)) % n for i in range(n - 1)]

    vis = [0] * n
    st = [0] * n

    def dfs(g, e):
        if vis[e] == 1:
            return
        vis[e] = 1
        for i in g[e]:
            dfs(g, i)
        if len(g[e]) == 1 and e != 0:
            st[e] += 1
        for i in g[e]:
            st[e] += st[i]

    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[i + 1].append(a[i])
        g[a[i]].append(i + 1)

    dfs(g, 0)
    st.sort()
    print(*st)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)