import math

def build_tree(n):
    # Build a simple deterministic tree: a path 1-2-3-...-n
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))
    return edges

def check_structure(n, k, edges):
    degreelist = []
    for i in range(min(k + 1, math.floor(math.log2(n)) + 10)):
        degreelist.append({})
    degrees = degreelist[0]
    for i in range(1, n + 1):
        degrees[i] = 0
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    small = []
    center = None
    done = False

    for i in range(k):
        if not done:
            small = []
            for guy in degrees:
                if degrees[guy] == 2:
                    return False
                if degrees[guy] == 3:
                    small.append(guy)
                    if center is None:
                        center = guy
                    elif center != guy:
                        return False
                elif degrees[guy] > 1:
                    small.append(guy)
            degrees = degreelist[i + 1]
            if center is not None and center not in small:
                return False
            elif len(small) == 0:
                return False
            for guy in small:
                degrees[guy] = 0
            for u, v in edges:
                if u in degrees and v in degrees:
                    degrees[u] += 1
                    degrees[v] += 1
            for guy in degrees:
                if degrees[guy] > 1 and degreelist[i][guy] != degrees[guy]:
                    return False

        else:
            break
    if not done:
        if len(degreelist[-1]) == 1:
            return True

        else:
            return False

def main(n):
    # Interpret n as the number of nodes in a tree.
    # Set k deterministically as floor(log2(n)) for scaling.
    if n < 2:
        n = 2
    k = max(1, int(math.log2(n)))
    edges = build_tree(n)
    ok = check_structure(n, k, edges)
    # print("Yes" if ok else "No")
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)