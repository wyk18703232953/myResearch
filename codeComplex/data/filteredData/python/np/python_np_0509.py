from collections import defaultdict, deque
import random
import string

class Graph:
    def __init__(self, N, M=-1):
        self.V = N
        if M >= 0:
            self.E = M
        self.edge = [[] for _ in range(self.V)]
        self.edge_rev = [[] for _ in range(self.V)]
        self.order = []
        self.to = [0] * self.V
        self.visited = [False] * self.V
        self.dp = [0] * self.V

    def add_edge(self, a, b, dist=-1, bi=False, rev=False):
        if dist >= 0:
            self.edge[a].append((dist, b))
            if rev:
                self.edge_rev[b].append((dist, a))
            if bi:
                self.edge[b].append((dist, a))
        else:
            self.edge[a].append(b)
            self.to[b] += 1
            if rev:
                self.edge_rev[b].append(a)
            if bi:
                self.edge[b].append(a)

    def topo_sort(self):  # topological sort
        updated = [0] * self.V
        for start in range(self.V):
            if self.to[start] or updated[start]:
                continue
            stack = deque([start])
            while stack:
                v = stack.popleft()
                self.order.append(v + 1)
                updated[v] = 1
                for u in self.edge[v]:
                    self.to[u] -= 1
                    if self.to[u]:
                        continue
                    stack.append(u)


def generate_test_data(n):
    """
    根据规模 n 生成一组 (N, M, K, patterns, queries)
    patterns: 长度为 N 的字符串列表
    queries:  长度为 M 的 (t, mt) 列表
    """
    # 简单设定：K = min(4, n)，字符串字符从前 3 个小写字母中取
    K = max(1, min(4, n))
    N = n
    alphabet = 'abc'

    # 生成 N 个不重复的长度为 K 的模式串
    patterns_set = set()
    while len(patterns_set) < N:
        s = ''.join(random.choice(alphabet) for _ in range(K))
        patterns_set.add(s)
    patterns = list(patterns_set)
    N = len(patterns)

    # 为了使拓扑排序经常有解，构造 M 个查询，使得每个查询一定包含 mt 本身
    # 生成 M 与 N 同量级
    M = max(1, N * 2)

    queries = []
    for _ in range(M):
        # 随机挑一个模式作为 t 和 mt 的基底
        base_idx = random.randrange(N)
        t_list = list(patterns[base_idx])

        # 随机对 t 做部分扰动（保持在 alphabet 中），长度仍为 K
        for i in range(K):
            if random.random() < 0.3:
                t_list[i] = random.choice(alphabet)
        t = ''.join(t_list)

        # mt 是 base_idx（使得 mt 对应的模式一定出现在候选列表中）
        mt = base_idx + 1  # 原始程序中 mt 是 1-based
        queries.append((t, mt))

    return N, M, K, patterns, queries


def main(n):
    # 1. 生成测试数据
    N, M, K, patterns, queries = generate_test_data(n)

    # 2. 原始逻辑从这里开始
    dic = defaultdict(lambda: -1)
    for i in range(N):
        S = patterns[i]
        dic[S] = i

    G = Graph(N)

    for t, mt in queries:
        mt_idx = mt - 1  # 转回 0-based
        lis = []
        for S in range(1 << K):
            s = []
            for i in range(K):
                if (S >> i) & 1:
                    s.append('_')
                else:
                    s.append(t[i])
            s = ''.join(s)
            if dic[s] >= 0:
                lis.append(dic[s])

        if mt_idx not in lis:
            print('NO')
            return

        for l in lis:
            if l != mt_idx:
                G.add_edge(mt_idx, l, bi=False, rev=False)

    G.topo_sort()
    if len(G.order) == N:
        print('YES')
        print(*G.order)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：n 可自行调整
    main(10)