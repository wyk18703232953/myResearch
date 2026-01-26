import sys


def run_algorithm(n, edges):
    deg = [0] * n
    if n == 2:
        # print('Yes')
        pass
        # print(1)
        pass
        # print('1 2')
        pass
        return

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    ix = deg.index(max(deg))

    if deg[ix] < 3 or deg.count(1) + deg.count(2) == n - 1:
        cnt1 = deg.count(1)
        # print('Yes')
        pass
        # print(cnt1)
        pass
        for i in range(n):
            if deg[i] == 1:
                # print(i + 1, ix + 1)
                pass

    else:
        # print('No')
        pass


def build_input(n):
    if n < 2:
        n = 2

    edges = []
    if n == 2:
        edges.append((1, 2))
        return n, edges

    # Build a star-like tree where node 1 has high degree when n is large
    # For determinism and scalability, connect node 1 with nodes 2..n
    for v in range(2, n + 1):
        edges.append((1, v))

    return n, edges


def main(n):
    n, edges = build_input(n)
    run_algorithm(n, edges)


if __name__ == "__main__":
    # example deterministic call
    main(10)