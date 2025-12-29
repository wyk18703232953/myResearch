import random

def push(d, u, v):
    if u not in d:
        d[u] = []
    if v not in d:
        d[v] = []
    d[u].append(v)
    d[v].append(u)

def push_v(d, u, val):
    if u not in d:
        d[u] = 0
    d[u] += val

def solve(n, k, edges):
    g = {}
    for u, v in edges:
        push(g, u, v)

    deg1 = []
    used = [0] * (n + 1)

    for u in g:
        if len(g[u]) == 1:
            used[u] = 1
            deg1.append(u)

    flg = True
    kk = k
    while kk > 0:
        if kk >= 1 and len(deg1) < 3:
            flg = False
            break

        cnt = {}
        for u in deg1:
            for v in g[u]:
                if used[v] == 0:
                    push_v(cnt, v, 1)

        for v in deg1:
            used[v] = 1

        deg1 = []

        for v, val in cnt.items():
            if val < 3:
                flg = False
                break
            deg1.append(v)

        if flg is False:
            break
        kk -= 1

    if flg is True and len(deg1) > 1:
        flg = False

    return "YES" if flg else "NO"

def generate_random_tree(n):
    edges = []
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        edges.append((u, v))
    return edges

def main(n):
    # 示例：规模 n 控制节点数，k 可根据需要设定/变化
    # 这里设定 k 为随机值 [0, n] 内
    if n < 1:
        return

    k = random.randint(0, n)
    edges = generate_random_tree(n)
    ans = solve(n, k, edges)
    print(ans)

if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(10)