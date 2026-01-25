from queue import Queue

def main(n):
    if n <= 0:
        return

    # 构造一棵确定性的树：1 为根，其余节点顺序连接形成链 1-2-3-...-n
    g = [set() for _ in range(n + 1)]
    for i in range(1, n):
        u = i
        v = i + 1
        g[u].add(v)
        g[v].add(u)

    # 构造一个确定性的访问序列 a
    # 这里使用从 1 到 n 的升序遍历，保证是树的一种合法 BFS/DFS 顺序
    a = list(range(1, n + 1))

    # 以下为原算法主体逻辑
    if a[0] != 1:
        print("No")
        return
    ptr = 0
    i = 1

    while i < n:
        par = a[ptr]
        while len(g[par]) != 0:
            if i >= n or a[i] not in g[par]:
                print("No")
                return
            else:
                g[par].remove(a[i])
                g[a[i]].remove(par)
            i += 1
        ptr += 1
    print("Yes")


if __name__ == "__main__":
    # 示例：对若干规模进行调用
    for size in [1, 2, 5, 10]:
        print(f"n = {size}")
        main(size)