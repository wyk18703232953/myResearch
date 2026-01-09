def main(n):
    from collections import defaultdict

    # Deterministically generate parent array for a tree of size n
    # par[i] is parent of node (i+2), nodes are 1..n
    # Here we build a simple pattern: parent of node i (i>=2) is i//2
    if n <= 1:
        # For n = 1, there is only the root node
        par = []

    else:
        par = [i // 2 for i in range(2, n + 1)]  # length n-1

    graph = defaultdict(list)
    bulb = [1] * (n + 1)

    for i in range(n - 1):
        bulb[par[i]] = 0
        graph[par[i]].append(i + 2)

    zero = bulb.count(0)
    for i in range(n, 0, -1):
        if bulb[i] == 0:
            count = 0
            for j in graph[i]:
                count += bulb[j]
            bulb[i] = count

    bulb = bulb[1:]
    bulb.sort()
    # print(' '.join(map(str, bulb)))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)