import sys
import random

sys.setrecursionlimit(10**5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
inf = 10**16
md = 10**9 + 7

trie = [{}]
k = 0  # will be set inside main


def push(s, val):
    now = 0
    for c in s:
        if c not in trie[now]:
            trie[now][c] = len(trie)
            trie.append({})
        now = trie[now][c]
    trie[now]["end"] = val


def match(s):
    res = []
    stack = [(0, 0)]
    while stack:
        u, i = stack.pop()
        if i == k:
            if "end" in trie[u]:
                res.append(trie[u]["end"])
            continue
        if s[i] in trie[u]:
            stack.append((trie[u][s[i]], i + 1))
        if "_" in trie[u]:
            stack.append((trie[u]["_"], i + 1))
    return res


def generate_test_data(n):
    """
    生成规模为 n 的测试数据：
    - n: 模式字符串数量，也作为节点数量
    - m: 生成的约束数量，取 2n
    - k: 字符串长度，固定为 3
    保证：
    - 所有模式长度为 k
    - 所有查询字符串长度为 k
    - 仅使用小写字母和 '_'（通配符）
    - 结构基本无环，最后再随机加一些额外边（可能造成 NO）
    """
    random.seed(0)
    global k
    k = 3

    letters = "abc"
    patterns = []
    for i in range(n):
        s = "".join(random.choice(letters) for _ in range(k))
        patterns.append(s)

    m = max(1, 2 * n)
    queries = []
    for _ in range(m):
        # 以一定概率生成和某个已有模式完全匹配的字符串
        if random.random() < 0.7:
            base_idx = random.randrange(n)
            base = patterns[base_idx]
            s = list(base)
            # 以小概率在某些位置替换为 '_'
            for i in range(k):
                if random.random() < 0.2:
                    s[i] = '_'
            s = "".join(s)
            u = base_idx + 1  # 1-based for original logic
        else:
            # 纯随机字符串，无 '_'，较大概率导致 NO
            s = "".join(random.choice(letters) for _ in range(k))
            u = random.randrange(1, n + 1)
        queries.append((s, u))
    return n, m, k, patterns, queries


def main(n):
    global trie, k
    trie = [{}]

    # 生成测试数据
    n, m, k, patterns, queries = generate_test_data(n)

    # 构建 trie
    for i in range(n):
        push(patterns[i], i)

    # 构建有向图
    to = [[] for _ in range(n)]
    for s, u in queries:
        u -= 1  # 转为 0-based
        vv = match(s)

        notmatch = True
        for v in vv:
            if u == v:
                notmatch = False
            else:
                to[u].append(v)
        if notmatch:
            print("NO")
            return

    # 拓扑排序 + 有向环检测（迭代写法）
    vis = [-1] * n  # -1:未访问, 0:访问中, 1:已完成
    topo = []
    for start in range(n):
        if vis[start] == 1:
            continue
        stack = [start]
        while stack:
            u = stack.pop()
            if vis[u] == -1:
                vis[u] = 0
                stack.append(u)
                for v in to[u]:
                    if vis[v] == 0:
                        print("NO")
                        return
                    if vis[v] == -1:
                        stack.append(v)
            elif vis[u] == 0:
                topo.append(u + 1)  # 恢复为 1-based 输出
                vis[u] = 1

    print("YES")
    print(*topo[::-1])


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)