def check(prev, parent, curr, level, degrees, neighbors, k):
    if level == 0:
        return len(parent) == 1 and degrees[curr - 1] == 1, []
    checked = []
    for neighbor in neighbors[curr - 1]:
        if len(prev) != 0 and prev[0] == neighbor:
            checked.append(neighbor)
            continue
        if len(parent) != 0 and parent[0] == neighbor:
            continue
        result, _ = check([], [curr], neighbor, level - 1, degrees, neighbors, k)
        if result:
            checked.append(neighbor)
        else:
            if len(parent) == 0:
                parent.append(neighbor)
            else:
                return False, []
    if len(checked) > 2 and len(parent) == 0 and level == k:
        return True, []
    elif len(checked) > 2 and len(parent) == 1 and level != k:
        return True, parent
    else:
        return False, []


def build_deterministic_tree(n):
    # Build a deterministic tree with n nodes
    # Root = 1, for i >= 2, parent(i) = i//2
    degrees = [0] * n
    neighbors = [[] for _ in range(n)]
    for i in range(2, n + 1):
        p = i // 2
        degrees[p - 1] += 1
        degrees[i - 1] += 1
        neighbors[p - 1].append(i)
        neighbors[i - 1].append(p)
    return degrees, neighbors


def main(n):
    if n < 2:
        # trivial small case, still deterministic
        print("No")
        return

    # Choose k as a deterministic function of n
    # Ensure k >= 1 and not too large compared to n
    k = max(1, n // 4)

    degrees, neighbors = build_deterministic_tree(n)

    # start at a leaf
    curr = 0
    for i in range(n):
        if degrees[i] == 1:
            curr = i + 1
            break
    if curr == 0 or len(neighbors[curr - 1]) == 0:
        print("No")
        return
    curr = neighbors[curr - 1][0]

    prev = []
    parent = []
    counter = 1
    while counter <= k:
        result, parent = check(prev, [], curr, counter, degrees, neighbors, k)
        if not result:
            print("No")
            return
        if counter == k:
            print("Yes")
            return
        prev = [curr]
        curr = parent[0]
        counter += 1


if __name__ == "__main__":
    main(10)