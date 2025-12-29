from collections import deque
from types import GeneratorType
import random


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


def build_random_tree(n):
    """生成一个含 n 个节点的随机树，节点标签为 1..n"""
    if n <= 0:
        return {}
    graph = {i: [] for i in range(1, n + 1)}
    for v in range(2, n + 1):
        u = random.randint(1, v - 1)
        graph[u].append(v)
        graph[v].append(u)
    return graph


def main(n):
    # 1. 生成规模为 n 的测试数据（随机树）
    graph = build_random_tree(n)

    # 2. 定义 solve，需要访问 graph, visited, r
    visited = set()
    r = [0]

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

    # 3. 按原逻辑执行
    roots = []
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
        if i not in visited:
            r = [0]
            # 重新绑定 r 给 solve 使用
            @bootstrap
            def solve_local(node):
                cnt = 0
                visited.add(node)
                for k in graph[node]:
                    if k not in visited:
                        cnt += 1
                if cnt >= 1:
                    for k in graph[node]:
                        if k not in visited:
                            yield solve_local(k)
                            break
                else:
                    r[0] = node
                yield

            solve_local(i)
            ans.append([str(r[0]), str(ele)])

    if len(visited) == n:
        print("Yes")
        print(len(ans))
        for i in ans:
            print(" ".join(i))
    else:
        print("No")


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)