def main(n):
    from collections import defaultdict

    # Generate deterministic tree parent array for nodes 2..n
    # par[i] is parent of node i+2 (0-based index for par)
    if n <= 1:
        # Edge case: single node tree
        bulb = [1]
        # print(' '.join(map(str, bulb)))
        pass
        return

    par = [i // 2 + 1 for i in range(n - 1)]

    graph = defaultdict(list)
    bulb = [1] * (n + 1)

    for i in range(n - 1):
        bulb[par[i]] = 0
        graph[par[i]].append(i + 2)

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
    main(10)