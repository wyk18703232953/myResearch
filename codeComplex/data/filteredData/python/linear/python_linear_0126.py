def if_spruce(n, l, m):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        if m[i] == 0:
            d[l[i]] += 1
    for i in range(1, n + 1):
        if m[i] > 0 and d[i] < 3:
            return "No"
    return "Yes"


def generate_tree(n):
    # Generate a deterministic tree with n nodes (1..n)
    # Parent array l of size n+2 (to keep original indexing behavior)
    # m[i] = number of children of node i
    if n < 2:
        # For n=1, there are no edges; keep l and m consistent
        l = [0, 0]  # indices 0,1 used; 1 is root with parent 0
        m = [0, 0]
        return l, m

    # Start with placeholders to match original code's initial l=[0,0]
    l = [0, 0]
    m = [0] * (n + 1)

    # Deterministic parent assignment for nodes 2..n
    for i in range(2, n + 1):
        parent = i // 2
        l.append(parent)
        m[parent] += 1

    return l, m


def main(n):
    l, m = generate_tree(n)
    result = if_spruce(n, l, m)
    print(result)


if __name__ == "__main__":
    # Example deterministic call for experimental purposes
    main(10)