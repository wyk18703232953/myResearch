def main(n):
    # deterministic mapping from n -> (n_nodes, a, b)
    # ensure n_nodes >= 2
    n_nodes = max(2, n)
    # alternate between a>1, b==1 and a==1, b>1 to cover both branches
    if n_nodes % 2 == 0:
        a = 1
        b = max(1, (n_nodes // 3) or 1)

    else:
        b = 1
        a = max(1, (n_nodes // 3) or 1)

    # preserve original logic
    if a > 1 and b > 1:
        # print('NO')
        pass
        return

    if n_nodes == 3 and a == 1 and b == 1:
        # print('NO')
        pass
        return

    if n_nodes == 2 and a == 1 and b == 1:
        # print('NO')
        pass
        return

    t = [[0 for _ in range(n_nodes)] for _ in range(n_nodes)]

    comp = max(a, b)

    for i in range(comp - 1, n_nodes - 1):
        t[i][i + 1] = 1
        t[i + 1][i] = 1

    if b > 1:
        for i in range(n_nodes):
            for j in range(n_nodes):
                if i != j:
                    t[i][j] = 1 - t[i][j]

    # print('YES')
    pass
    for i in range(n_nodes):
        # print("".join(map(str, t[i])))
        pass
if __name__ == "__main__":
    main(5)