from collections import defaultdict

def main(n):
    # Interpret n as the number of nodes in the tree
    # Construct a deterministic tree and a deterministic k
    if n < 2:
        # For n < 2, the original logic (which expects n-1 edges) is degenerate.
        # We set a minimal tree with 2 nodes.
        n = 2

    # Deterministic choice of k based on n
    # Ensure k is non-negative and scales with n
    k = n // 3

    connections = defaultdict(set)

    # Deterministic tree construction:
    # Use a star centered at 1 if n is small, otherwise a simple chain
    if n <= 10:
        # Star: 1 connected to all others
        for v in range(2, n + 1):
            connections[1].add(v)
            connections[v].add(1)

    else:
        # Chain: 1-2-3-...-n
        for u in range(1, n):
            v = u + 1
            connections[u].add(v)
            connections[v].add(u)

    leafs = set()
    for node in connections:
        if len(connections[node]) == 1:
            leafs.add(node)

    steps = 0
    is_correct = True
    while is_correct and steps <= k:
        new_leafs = set()
        for x in leafs:
            if len(connections[x]) > 1:
                is_correct = False
                break
            root = list(connections[x])[0]
            if len(connections[root]) < 4 and len(leafs) != 3:
                is_correct = False
                break
        if not is_correct:
            break
        for x in leafs:
            root = list(connections[x])[0]
            new_leafs.add(root)
            connections[root].remove(x)
        leafs = new_leafs
        steps += 1
        if len(leafs) == 1 and len(connections[list(leafs)[0]]) == 0:
            break

    if is_correct and steps == k:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)