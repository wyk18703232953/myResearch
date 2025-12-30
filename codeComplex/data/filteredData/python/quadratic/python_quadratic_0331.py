from sys import exit
import random

node = 1

def bad():
    print("NO")
    exit()

def make_branch(u, d, deg, g, n, k):
    global node
    # extend from node u with depth limit d while degree < k and node index < n
    while deg[u] < k and d > 0 and node < n:
        node += 1
        deg[u] += 1
        deg[node] = 1
        g[u].append(node)
        make_branch(node, d - 1, deg, g, n, k)

def solve(n, d, k):
    global node
    if d >= n or (k == 1 and n > 2):
        bad()

    g = [[] for _ in range(n + 5)]
    deg = [0 for _ in range(n + 5)]

    # build backbone path of length d+1
    for i in range(1, d + 1):
        g[i].append(i + 1)
        deg[i] += 1
        deg[i + 1] += 1

    node = d + 1

    LD = 1
    RD = d - 1
    for u in range(2, d + 1):
        make_branch(u, min(LD, RD), deg, g, n, k)
        LD += 1
        RD -= 1

    used = [False for _ in range(n + 5)]
    q = [[1, 1]]
    used[1] = True
    while q:
        u, p = q.pop()
        for v in g[u]:
            if v != p:
                used[v] = True
                q.append([v, u])

    for i in range(1, n + 1):
        if not used[i]:
            bad()

    print("YES")
    for u in range(1, n + 1):
        for v in g[u]:
            print(u, v)

def main(n):
    # 根据规模 n 生成测试数据 (n, d, k)
    # 约束条件源自原逻辑:
    # 1) d < n
    # 2) 若 n > 2 则 k > 1
    # 3) k 不能太小以至于主链无法容纳：d+1 <= 1 + d*k  => k >= 1
    if n <= 1:
        # trivial smallest valid case: n=1, d=0, k任意>=1
        d = 0
        k = 1
    elif n == 2:
        # path of length 1, degree bound >=1
        d = 1
        k = 1
    else:
        # choose a diameter roughly sqrt(n)
        d = max(1, min(n - 1, int(n ** 0.5)))
        # ensure k>1 for n>2, and not too small
        k_min = 2
        k_max = max(k_min, min(5, n - 1))
        k = random.randint(k_min, k_max)

    solve(n, d, k)

if __name__ == "__main__":
    # 示例调用：可在此修改 n 以测试不同规模
    main(10)