import random
from enum import Enum


class flag(Enum):
    UNVISITED = -1
    EXPLORED = -2
    VISITED = -3


def match(p, s):
    for i in range(len(p)):
        if p[i] != "_" and p[i] != s[i]:
            return False
    return True


def cycleCheck(u, AL, dfs_num, dfs_parent, sol_ref):
    dfs_num[u] = flag.EXPLORED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            dfs_parent[v] = u
            cycleCheck(v, AL, dfs_num, dfs_parent, sol_ref)
        elif dfs_num[v] == flag.EXPLORED.value:
            sol_ref[0] = False
    dfs_num[u] = flag.VISITED.value


def toposort(u, AL, dfs_num, ts):
    dfs_num[u] = flag.VISITED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            toposort(v, AL, dfs_num, ts)
    ts.append(u)


def generate_patterns(n, length=4):
    # 生成 n 个长度为 length 的模式串，字符集为小写字母与 '_'
    patterns = []
    ps = set()
    alphabet = "abc"
    while len(patterns) < n:
        p = ''.join(random.choice(alphabet + "_") for _ in range(length))
        if p not in ps:
            ps.add(p)
            patterns.append(p)
    return patterns


def generate_queries(n, m, k, pa):
    # 随机生成 m 条查询 (s, fn)
    # s 长度与模式长度相同，字符集为小写字母
    queries = []
    alphabet = "abc"
    length = len(pa[0])
    for _ in range(m):
        s = ''.join(random.choice(alphabet) for _ in range(length))
        fn = random.randint(1, n)
        queries.append((s, fn))
    return queries


def main(n):
    # n: 模式数量规模
    # 为了和原程序一致，再生成 m、k（k 未实际使用）
    random.seed(0)
    m = max(1, n * 2)
    k = 0  # 原程序未使用 k，仅占位

    # 1. 生成测试数据
    pa = generate_patterns(n)      # 模式数组
    ps = set(pa)                   # 模式集合
    pd = {p: i + 1 for i, p in enumerate(pa)}  # 模式到编号的映射（1-based）

    queries = generate_queries(n, m, k, pa)

    # 2. 按原逻辑构建图并检查
    AL = [[] for _ in range(n)]
    sol_ref = [True]  # 使用列表封装以在递归中修改

    for s, fn in queries:
        if not match(pa[fn - 1], s):
            sol_ref[0] = False

        mm = [""]
        for ch in s:
            mm = list(map(lambda x: x + "_", mm)) + list(map(lambda x: x + ch, mm))
        for pattern in mm:
            if pattern in ps and pd[pattern] != fn:
                AL[fn - 1].append(pd[pattern] - 1)

    try:
        if not sol_ref[0]:
            print("NO")
            return

        dfs_num = [flag.UNVISITED.value] * n
        dfs_parent = [-1] * n

        for u in range(n):
            if dfs_num[u] == flag.UNVISITED.value:
                cycleCheck(u, AL, dfs_num, dfs_parent, sol_ref)

        if not sol_ref[0]:
            print("NO")
            return

        dfs_num = [flag.UNVISITED.value] * n
        ts = []
        for u in range(n):
            if dfs_num[u] == flag.UNVISITED.value:
                toposort(u, AL, dfs_num, ts)
        ts.reverse()

        print("YES")
        print(' '.join(str(x + 1) for x in ts))
    except Exception:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)