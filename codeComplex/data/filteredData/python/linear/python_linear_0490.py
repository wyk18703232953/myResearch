def main(n):
    if n <= 3:
        print(0)
        return

    # 构造一个确定性的树：长链结构 1-2-3-...-n
    # 节点在原程序中是 1..n，内部使用 0..n-1
    g = {}
    for i in range(1, n):
        u = i
        v = i + 1
        g.setdefault(u - 1, []).append(v - 1)
        g.setdefault(v - 1, []).append(u - 1)

    st = [0]
    rank = [0] * n
    tree = [0] * n
    msk = [0] * n
    rd = {}

    while st:
        top = st.pop()
        msk[top] = 1
        for c in g.get(top, []):
            if msk[c] == 0:
                st.append(c)
                tree[c] = top
                rank[c] = rank[top] + 1
                rd.setdefault(rank[c], []).append(c)

    max_rank = max(rank)
    reach = [0] * n
    build = [0] * n

    for r in range(max_rank, 2, -1):
        for node in rd.get(r, []):
            if reach[node] == 0:
                reach[node] = 1
                reach[tree[node]] = 1
                reach[tree[tree[node]]] = 1
                build[tree[node]] = 1

    print(sum(build))


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值进行实验
    main(10)