def main(n):
    # Interpret n as the number of nodes; deterministically derive d and k from n
    if n < 3:
        d = 1
        k = 1

    else:
        d = max(1, n // 4)
        k = max(1, min(5, n // 3))

    # Original logic starts here, with (n, d, k) generated from n
    if n == 2 and d == 1 and k == 1:
        # print("YES")
        pass
        # print("1 2")
        pass
        return

    if n == d + 1 and k - 1:
        # print("YES")
        pass
        for i in range(1, d + 1):
            # print(i, i + 1)
            pass
        return

    if n < d + 1 or k <= 2 or d == 1:
        # print("NO")
        pass
        return

    if d % 2 == 0:
        if n * (k - 2) > -2 + k * (k - 1) ** (d // 2):
            # print("NO")
            pass
            return
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
                    if nodes == n:
                        return
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 1 + dev + d // 2]

    else:
        if n * (k - 2) > -2 + k * (k - 1) ** (d // 2) + (k - 2) * (k - 1) ** (d // 2):
            # print("NO")
            pass
            return
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
                    if nodes == n:
                        return
            dev += 1
            leaves = new_leaves + [1 - dev + d // 2, 2 + dev + d // 2]


if __name__ == "__main__":
    # Example deterministic call; change 20 to any n you want to test
    main(20)