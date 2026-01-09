def main(n):
    # n: number of vertices in a tree
    if n < 1:
        # print("No")
        pass
        return

    # Deterministic tree construction:
    # Build a simple path 1-2-3-...-n
    graph = [set() for _ in range(n + 2)]
    for i in range(1, n):
        x = i
        y = i + 1
        graph[x].add(y)
        graph[y].add(x)

    # Deterministic sequence a:
    # Original logic expects a BFS-like traversal starting from 1.
    # For a path 1-2-...-n, the only valid sequence is 1,2,3,...,n.
    a_list = list(range(1, n + 1))
    a = iter(a_list)

    try:
        assert next(a) == 1
        q = [1]
        for v in q:
            gv = graph[v]
            gv1 = tuple(gv)
            for tr2 in gv1:
                u = next(a)
                assert u in gv
                gv.remove(u)
                graph[u].remove(v)
                q.append(u)
        # print("Yes")
        pass
    except (AssertionError, StopIteration):
        # print("No")
        pass
if __name__ == "__main__":
    # Example call for scalability/time experiments
    # Adjust n as needed
    main(10)