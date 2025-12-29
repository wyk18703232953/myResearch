import random

def main(n):
    # 生成一棵 n 个节点的随机树（节点编号 0..n-1）
    # 使用随机生成的父节点构造树：对于每个 i>0，连一条边 (i, p) 其中 p<i
    g = dict()
    for i in range(1, n):
        p = random.randint(0, i - 1)
        g.setdefault(i, []).append(p)
        g.setdefault(p, []).append(i)
    for i in range(n):
        g.setdefault(i, [])

    st = [0]
    rank = [0] * n
    tree = [0] * n
    msk = [0] * n
    rd = dict()

    # 构建树的父节点和深度信息
    while st:
        top = st.pop()
        msk[top] = 1
        for c in g[top]:
            if msk[c] == 0:
                st.append(c)
                tree[c] = top
                rank[c] = rank[top] + 1
                rd.setdefault(rank[c], []).append(c)

    max_rank = max(rank)
    reach = [0] * n
    build = [0] * n

    # 自底向上选择节点
    for r in range(max_rank, 2, -1):
        for node in rd.get(r, []):
            if reach[node] == 0:
                reach[node] = 1
                reach[tree[node]] = 1
                reach[tree[tree[node]]] = 1
                build[tree[node]] = 1

    ans = sum(build)
    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的随机树
    main(10)