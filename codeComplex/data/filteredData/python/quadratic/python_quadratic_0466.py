from queue import Queue

def main(n):
    if n < 2:
        # print("Yes")
        pass
        return

    # 构造一棵确定性的树：链状 1-2-3-...-n
    g = [set() for _ in range(n + 1)]
    for u in range(1, n):
        v = u + 1
        g[u].add(v)
        g[v].add(u)

    # 构造一个确定性的 BFS 序列（对于链来说就是 1,2,...,n）
    a = list(range(1, n + 1))

    if a[0] != 1:
        # print("No")
        pass
        return

    ptr = 0
    i = 1

    while i < n:
        par = a[ptr]
        while len(g[par]) != 0:
            if i >= n or a[i] not in g[par]:
                # print("No")
                pass
                return
            g[par].remove(a[i])
            g[a[i]].remove(par)
            i += 1
        ptr += 1
    # print("Yes")
    pass
if __name__ == "__main__":
    main(10)