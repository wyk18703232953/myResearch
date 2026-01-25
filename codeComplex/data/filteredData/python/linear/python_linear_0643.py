def main(n):
    # n: number of nodes
    if n <= 0:
        return

    # Deterministic construction of array a of length n.
    # Interpretation based on original code:
    # - positions with a[i] == 1 are leaves
    # - positions with a[i] != 1 are "roots" and a[i]-2 is initial capacity
    #
    # Here we:
    # - ensure at least one root when n >= 2
    # - distribute capacities in a simple, deterministic way.
    a = [1] * n
    if n >= 2:
        # Make positions with index % 3 != 0 roots with varying capacities
        for i in range(n):
            if i % 3 != 0:
                # capacity pattern: 1,2,3,1,2,3,...
                cap = (i % 3) + 1
                a[i] = cap + 2  # since root_r uses a[i]-2 as capacity

    leaf = [i + 1 for i in range(n) if a[i] == 1]
    root_w = [i + 1 for i in range(n) if a[i] != 1]
    root_r = [a[i - 1] - 2 for i in root_w]
    l_path = root_w[:]

    if len(leaf) != 0:
        l_path = [leaf[0]] + l_path
        leaf = leaf[1:]
    if len(leaf) != 0:
        l_path = l_path + [leaf[0]]
        leaf = leaf[1:]

    if sum(root_r) < len(leaf):
        print("NO")
    else:
        print("YES {}".format(len(l_path) - 1))
        print(n - 1)
        for i in range(len(l_path) - 1):
            print("{} {}".format(l_path[i], l_path[i + 1]))
        for l in leaf:
            while len(root_r) > 0 and root_r[0] == 0:
                root_w = root_w[1:]
                root_r = root_r[1:]
            print("{} {}".format(l, root_w[0]))
            root_r[0] = root_r[0] - 1


if __name__ == "__main__":
    # Example deterministic runs for time-complexity experiments
    for size in [1, 2, 5, 10]:
        main(size)