from collections import deque
from types import GeneratorType
import sys
import random
import __pypy__  # type: ignore

EPS = 10**-12


def bootstrap(f, stack=[]):
    # Deep recursion helper for generators.
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


class CycleFindDirected(object):
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        assert 0 <= u < self.n
        assert 0 <= v < self.n
        self.adj[u].append(v)

    @bootstrap
    def dfs(self, node):
        self.color[node] = 1
        for i in self.adj[node]:
            if self.color[i] == 0:
                self.parent[i] = node
                if (yield self.dfs(i)):
                    yield True
            elif self.color[i] == 1:
                self.cycle_end = node
                self.cycle_start = i
                yield True
        self.color[node] = 2
        yield False

    def find(self):
        self.color = [0] * self.n
        self.parent = [-1] * self.n
        self.cycle_end = -1
        self.cycle_start = -1

        for i in range(self.n):
            if not self.color[i] and self.dfs(i):
                answer = []
                node_begin = self.cycle_start
                node_end = self.cycle_end
                answer.append(node_begin)
                while node_end != node_begin:
                    answer.append(node_end)
                    node_end = self.parent[node_end]

                answer.reverse()
                if len(answer) == 1:
                    # self-loop special case
                    return [node_begin, node_begin]
                return answer
        return None


def main(n):
    """
    自动生成规模为 n 的测试数据，并执行原逻辑。
    这里生成一个随机有向图：
    - 顶点数: n
    - 边数: m 约为 n 到 2n 之间（但最多 n*(n-1)）
    """
    random.seed(1)

    # 限制 n，避免极端情况
    n = max(1, n)
    max_edges = n * (n - 1)
    m = random.randint(n, min(2 * n, max_edges)) if max_edges > 0 else 0

    # 随机生成有向边（可能有重复边，逻辑与原程序兼容）
    edges = []
    base = CycleFindDirected(n)
    for _ in range(m):
        u = random.randrange(n)
        v = random.randrange(n)
        edges.append((u, v))
        base.add_edge(u, v)

    # 以下为原 main 的逻辑（不再使用输入输出封装）
    cycle = base.find()
    if not cycle:
        print("YES")
        return

    cycle.append(cycle[0])

    bad_edges = set()
    cycle_edges = []
    for u, v in zip(cycle[:-1], cycle[1:]):
        bad_edges.add((u, v))
        cycle_edges.append((u, v))

    cf = CycleFindDirected(n)
    for edge in edges:
        if edge not in bad_edges:
            cf.add_edge(edge[0], edge[1])

    for edge in cycle_edges:
        # 临时加入除当前 edge 外的所有环边
        for toadd in cycle_edges:
            if toadd != edge:
                cf.adj[toadd[0]].append(toadd[1])

        if not cf.find():
            print("YES")
            return

        # 撤销刚才加入的边
        for toadd in cycle_edges:
            if toadd != edge:
                cf.adj[toadd[0]].pop()

    print("NO")


if __name__ == "__main__":
    # 示例：可以手动调整 n 进行快速测试
    main(5)