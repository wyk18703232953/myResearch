from collections import deque
import random

MAX = int(10e5 + 42)

# 全局变量（保持原结构）
n = 0
m = 0
u = [0] * MAX
v = [0] * MAX
c = [0] * MAX
g = [[] for _ in range(MAX)]
dag = [0] * MAX
top = [0] * MAX


def top_sort():
    global dag, top, g, n
    q = deque()
    cnt = 0

    for i in range(1, n + 1):
        if not dag[i]:
            q.append(i)

    while q:
        u_node = q.popleft()
        cnt += 1
        top[u_node] = cnt
        for to in g[u_node]:
            dag[to] -= 1
            if dag[to] == 0:
                q.append(to)
    return cnt == n


# creates graph with edges w < mid
def check(mid):
    global n, m, g, u, v, c, dag
    for i in range(1, n + 1):
        g[i].clear()
        dag[i] = 0
    for i in range(1, m + 1):
        if c[i] > mid:
            g[u[i]].append(v[i])
            dag[v[i]] += 1
    return top_sort()


def main(n_param: int):
    """
    n_param: 规模参数，用于生成测试数据的点数 n。
    测试数据生成策略：
      - 顶点数 n = n_param（至少为 2）
      - 边数 m = min(MAX-1, n*(n-1)//2) 的一部分，约为 n 的 2 倍
      - 随机生成有向图和边权
    """
    global n, m, u, v, c, g, dag, top

    # 设置随机种子以便复现（如需不同数据可改为不设种子）
    random.seed(0)

    n = max(2, n_param)  # 保证至少 2 个点
    # 生成边数：这里取 2*n，且不超过最大可能边数和 MAX-1
    max_possible_edges = n * (n - 1) // 2
    m = min(2 * n, max_possible_edges, MAX - 1)

    # 生成一个简单的随机有向无自环图，允许重复边但不会影响算法正确性
    max_weight = n  # 边权范围 [1, max_weight]
    for i in range(1, m + 1):
        while True:
            uu = random.randint(1, n)
            vv = random.randint(1, n)
            if uu != vv:
                break
        w = random.randint(1, max_weight)
        u[i], v[i], c[i] = uu, vv, w

    # 初始化辅助数组（长度足够大，前 n 部分会被使用）
    for i in range(1, n + 1):
        g[i].clear()
        dag[i] = 0
        top[i] = 0

    # 二分查找
    r = 0
    for i in range(1, m + 1):
        if c[i] > r:
            r = c[i]
    l = 0
    cnt = 0

    while l < r:
        mid = (l + r) >> 1
        if check(mid):
            r = mid
        else:
            l = mid + 1

    check(l)
    for i in range(1, m + 1):
        if c[i] <= l and top[v[i]] < top[u[i]]:
            cnt += 1

    print(f"{l} {cnt}")
    for i in range(1, m + 1):
        if c[i] <= l and top[v[i]] < top[u[i]]:
            print(i, end=" ")
    print()


# 示例调用（实际评测时可由外部调用 main）
if __name__ == "__main__":
    main(10)