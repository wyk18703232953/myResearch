from collections import deque
from types import GeneratorType

def bfs(start, graph, explored, e):
    queue = deque([start])
    visited = {start}
    ele = 0
    while queue:
        node = queue.popleft()
        explored.add(node)
        neighbours = graph[node]
        cnt = 0
        for neighbour in neighbours:
            if neighbour not in visited and neighbour not in explored:
                cnt += 1

        if e[0] == 0 and cnt != 1:
            ele = node
            break

        else:
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    return ele


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


def build_tree(n):
    # Deterministically build a tree:
    # For n >= 1, nodes are 1..n
    # For i in 2..n, connect i with i//2 (forms a rooted tree)
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(2, n + 1):
        p = i // 2
        graph[p].append(i)
        graph[i].append(p)
    return graph


def run_algorithm(graph):
    n = len(graph)

    @bootstrap
    def solve(i):
        cnt = 0
        visited.add(i)
        for k in graph[i]:
            if k not in visited:
                cnt += 1

        if cnt >= 1:
            for k in graph[i]:
                if k not in visited:
                    yield solve(k)
                    break

        else:
            r[0] = i
        yield

    roots = []
    visited = set()
    ele = 0
    e = [ele]
    for i in graph:
        if len(graph[i]) == 1:
            roots.append(i)

    if not roots:
        return "No\n"

    x = roots[0]
    ans = []
    ele = bfs(x, graph, visited, e)
    ans.append((str(x), str(ele)))

    for i in graph[ele]:
        r = [0]
        if i not in visited:
            solve(i)
            ans.append([str(r[0]), str(ele)])

    out_lines = []
    if len(visited) == n:
        out_lines.append("Yes")
        out_lines.append(str(len(ans)))
        for pair in ans:
            out_lines.append(" ".join(pair))

    else:
        out_lines.append("No")
    return "\n".join(out_lines) + "\n"


def main(n):
    if n <= 0:
        # print("No")
        pass
        return
    graph = build_tree(n)
    result = run_algorithm(graph)
    # print(result, end='')
    pass
if __name__ == "__main__":
    # Example deterministic call for testing / scaling
    main(10)