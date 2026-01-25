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


@bootstrap
def solve(i, graph, visited, r):
    cnt = 0
    visited.add(i)
    for k in graph[i]:
        if k not in visited:
            cnt += 1

    if cnt >= 1:
        for k in graph[i]:
            if k not in visited:
                yield solve(k, graph, visited, r)
                break
    else:
        r[0] = i

    yield


def build_tree_graph(n):
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(2, n + 1):
        parent = i // 2
        graph[parent].append(i)
        graph[i].append(parent)
    return graph


def main(n):
    if n <= 1:
        print("No")
        return

    global_graph = build_tree_graph(n)
    graph = global_graph

    roots = []
    visited = set()
    ele = 0
    e = [ele]

    for i in graph:
        if len(graph[i]) == 1:
            roots.append(i)

    if not roots:
        print("No")
        return

    x = roots[0]
    ans = []
    ele = bfs(x, graph, visited, e)
    ans.append((str(x), str(ele)))

    for i in graph[ele]:
        r = [0]
        if i not in visited:
            solve(i, graph, visited, r)
            ans.append([str(r[0]), str(ele)])

    if len(visited) == n:
        print("Yes")
        print(len(ans))
        for i in ans:
            print(" ".join(i))
    else:
        print("No")


if __name__ == "__main__":
    main(10)