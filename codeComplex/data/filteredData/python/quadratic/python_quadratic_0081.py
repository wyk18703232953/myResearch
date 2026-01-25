import math
import heapq
import functools
from collections import deque
from types import GeneratorType

EPS = 10**-12


def bootstrap(f, stack=[]):
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
                    return [node_begin, node_begin]
                return answer
        return None


def core_logic(n, edges):
    base = CycleFindDirected(n)
    for (u, v) in edges:
        base.add_edge(u, v)

    cycle = base.find()
    if not cycle:
        return "YES"

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
        for toadd in cycle_edges:
            if toadd != edge:
                cf.adj[toadd[0]].append(toadd[1])
        if not cf.find():
            return "YES"
        for toadd in cycle_edges:
            if toadd != edge:
                cf.adj[toadd[0]].pop()

    return "NO"


def generate_dag_edges(n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if (i + j) % 3 == 0:
                edges.append((i, j))
    return edges


def generate_single_cycle_edges(n):
    edges = []
    for i in range(n):
        edges.append((i, (i + 1) % n))
    for i in range(n):
        for j in range(n):
            if i != j and (i + j) % 5 == 0 and (i, j) not in edges:
                edges.append((i, j))
    return edges


def generate_mixed_edges(n):
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            val = (i * 7 + j * 11) % (2 * n + 1)
            if val % 4 == 0:
                edges.append((i, j))
    return edges


def main(n):
    if n <= 1:
        nodes = max(2, n + 1)
        edges = generate_dag_edges(nodes)
    elif n % 3 == 0:
        nodes = n
        edges = generate_dag_edges(nodes)
    elif n % 3 == 1:
        nodes = n
        edges = generate_single_cycle_edges(nodes)
    else:
        nodes = n
        edges = generate_mixed_edges(nodes)

    result = core_logic(nodes, edges)
    print(result)


if __name__ == "__main__":
    main(10)