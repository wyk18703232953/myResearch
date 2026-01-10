def main(n):
    from collections import deque

    # Interpret n as number of nodes; derive k deterministically from n
    # Ensure a meaningful k while staying within bounds of the original logic
    if n < 2:
        k = 0
    else:
        k = max(1, n // 3)

    # Deterministically construct a tree with n nodes.
    # Example: star-like around node 0, with a path extension to vary structure.
    graph = [set() for _ in range(n)]
    if n >= 2:
        # First, connect node 0 with nodes 1..n-1 (star)
        for i in range(1, n):
            graph[0].add(i)
            graph[i].add(0)

        # Then modify deterministically to create some internal nodes and leaves pattern:
        # Rewire some edges into a path segment from node 1 to node (n-1)
        # while keeping the structure a tree.
        # For i from 2 to n-1, move connection from 0 to i-1.
        for i in range(2, n):
            if 0 in graph[i]:
                graph[0].remove(i)
                graph[i].remove(0)
                graph[i - 1].add(i)
                graph[i].add(i - 1)

    # Core algorithm unchanged, just using the generated graph and k
    leafs = [i for i, v in enumerate(graph) if len(v) == 1]
    new_leafs = []
    valid = True
    centers = dict()
    count = 0

    while len(leafs) > 1 and valid:
        for leaf in leafs:
            if not graph[leaf]:
                valid = False
                break

            center = next(iter(graph[leaf]))
            graph[leaf].remove(center)

            try:
                centers[center] += 1
            except KeyError:
                centers[center] = 1

            graph[center].remove(leaf)

            if len(graph[center]) == 0:
                break
            elif len(graph[center]) == 1:
                new_leafs.append(center)

        if not valid:
            break

        if any(mult < 3 for mult in centers.values()):
            valid = False
            break

        count = count + 1
        leafs = new_leafs
        new_leafs = []
        centers = {}

    if valid and count == k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)