n=0
s=0

def build_tree_edges(n):
    edges = []
    for i in range(2, n + 1):
        edges.append((i - 1, i))
    return edges

def main(n_input):
    global n, s
    n = max(2, n_input)
    s = n * (n + 1) // 2
    a = [0] * (n + 1)

    if n == 2:
        # print(s)
        pass
        return

    edges = build_tree_edges(n)
    for u, v in edges:
        a[u] += 1
        a[v] += 1

    # print(2.0 * s / a.count(1))
    pass
if __name__ == "__main__":
    main(10)