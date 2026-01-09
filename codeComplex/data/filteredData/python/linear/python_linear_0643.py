def main(n):
    # Generate deterministic input of size n
    # a[i] = 2 for even i, 1 for odd i (1-based index style in original code)
    a = [(2 if (i % 2 == 0) else 1) for i in range(n)]

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
        # print("NO")
        pass

    else:
        # print("YES {}".format(len(l_path) - 1))
        pass
        # print(n - 1)
        pass
        for i in range(len(l_path) - 1):
            # print("{} {}".format(l_path[i], l_path[i + 1]))
            pass
        for l in leaf:
            while len(root_r) > 0 and root_r[0] == 0:
                root_w = root_w[1:]
                root_r = root_r[1:]
            # print("{} {}".format(l, root_w[0]))
            pass
            root_r[0] = root_r[0] - 1


if __name__ == "__main__":
    main(10)