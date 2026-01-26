def main(n):
    if n < 1:
        # print("No")
        pass
        return

    # Generate a deterministic tree on vertices 1..n:
    # For i from 2 to n, connect i with i//2 to form a rooted tree at 1.
    graph = [set() for _ in range(n + 2)]
    for x in range(2, n + 1):
        y = x // 2
        graph[x].add(y)
        graph[y].add(x)

    # Generate a deterministic permutation of 2..n to simulate BFS order.
    # Use a simple linear congruential generator-like permutation.
    # This is fully deterministic and depends only on n.
    order = []
    if n >= 2:
        m = n - 1  # numbers to permute: 2..n  ->  map to 0..m-1
        a = 3      # multiplier, coprime with m when m is even; works as a simple generator for many n
        # Fall back to identity order if gcd(a, m) != 1, to keep logic simple & deterministic.
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        if gcd(a, m) != 1:
            # identity sequence: 2,3,...,n
            order = list(range(2, n + 1))

        else:
            visited = [False] * m
            cur = 0
            for _ in range(m):
                if visited[cur]:
                    break
                visited[cur] = True
                order.append(cur + 2)  # map back to 2..n
                cur = (cur + a) % m
            # If not all positions visited, append remaining in increasing index order
            for i in range(m):
                if not visited[i]:
                    order.append(i + 2)
    # Construct the input sequence 'a' that the original code reads:
    # first element must be 1, then all remaining vertices in some order.
    # This emulates a BFS-like traversal sequence.
    seq = [1] + order
    a_iter = iter(seq)

    try:
        assert next(a_iter) == 1
        q = [1]
        for v in q:
            gv = graph[v]
            gv1 = tuple(gv)
            for _ in gv1:
                u = next(a_iter)
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
    # Example deterministic calls
    for n in range(1, 8):
        # print(f"n = {n} -> ", end="")
        pass
        main(n)