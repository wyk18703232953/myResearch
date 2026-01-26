def main(n):
    # Deterministic mapping from n to (n_nodes, d, k)
    # Ensure parameters are valid and varied with n
    n_nodes = max(2, n)
    d = max(1, n // 3)
    k = max(1, n // 4)

    # Original logic with generated n_nodes, d, k
    if n_nodes == 2 and d == 1 and k == 1:
        # print("YES")
        pass
        # print("1 2")
        pass
        return 0
    if n_nodes == d + 1 and k - 1:
        # print("YES")
        pass
        for i in range(1, d + 1):
            # print(i, i + 1)
            pass
        return 0
    if n_nodes < d + 1 or k <= 2 or d == 1:
        # print("NO")
        pass
        return 0
    if d % 2 == 0:
        if n_nodes * (k - 2) > -2 + k * (k - 1) ** (d // 2):
            # print("NO")
            pass
            return 0
        # print("YES")
        pass
        for i in range(1, d + 1):
            # print(i, i + 1)
            pass
        nodes = d + 1
        leaves = [1 + d // 2]
        dev = 0
        while True:
            new_leaves = []
            for i in leaves:
                for j in range(k - 1 - (i <= d + 1)):
                    nodes += 1
                    # print(i, nodes)
                    pass
                    new_leaves.append(nodes)
                    if nodes == n_nodes:
                        return 0
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 1 + dev + d // 2]

    else:
        if n_nodes * (k - 2) > -2 + k * (k - 1) ** (d // 2) + (k - 2) * (k - 1) ** (d // 2):
            # print("NO")
            pass
            return 0
        # print("YES")
        pass
        for i in range(1, d + 1):
            # print(i, i + 1)
            pass
        nodes = d + 1
        leaves = [1 + d // 2, 2 + d // 2]
        dev = 0
        while True:
            new_leaves = []
            for i in leaves:
                for j in range(k - 1 - (i <= d + 1)):
                    nodes += 1
                    # print(i, nodes)
                    pass
                    new_leaves.append(nodes)
                    if nodes == n_nodes:
                        return 0
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 2 + dev + d // 2]


if __name__ == "__main__":
    main(10)