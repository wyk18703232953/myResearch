import sys


def solve(n, edges):
    deg = [0] * n
    if n == 2:
        return ["Yes", "1", "1 2"]

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    ix = deg.index(max(deg))

    if deg[ix] < 3 or deg.count(1) + deg.count(2) == n - 1:
        res = []
        res.append("Yes")
        res.append(str(deg.count(1)))
        for i in range(n):
            if deg[i] == 1:
                res.append(f"{i + 1} {ix + 1}")
        return res

    else:
        return ["No"]


def generate_tree_edges(n):
    if n <= 1:
        return []
    edges = []
    for i in range(2, n + 1):
        parent = (i // 2)
        if parent < 1:
            parent = 1
        edges.append((parent, i))
    return edges


def main(n):
    if n < 2:
        n = 2
    edges = generate_tree_edges(n)
    output_lines = solve(n, edges)
    for line in output_lines:
        # print(line)
        pass
if __name__ == "__main__":
    main(10)