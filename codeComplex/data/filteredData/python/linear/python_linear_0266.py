def main(n):
    # n is the number of nodes in a tree
    if n < 2:
        # print("No")
        pass
        return

    # Deterministically generate a tree with n nodes and n-1 edges
    # Pattern: for i in 2..n, connect i to (i // 2)
    edges = []
    deg = [0] * n
    for i in range(2, n + 1):
        u = i
        v = i // 2
        edges.append((u, v))
        deg[u - 1] += 1
        deg[v - 1] += 1

    coun = [0, deg.count(1), deg.count(2)]

    if n - coun[1] == 1:
        # print(f'Yes')
        pass
        # print(n - 1)
        pass
        for x in edges:
            # print(*x)
            pass
    elif coun[1] + coun[2] == n:
        # print('Yes')
        pass
        # print(1)
        pass
        # print(deg.index(1) + 1, n - deg[::-1].index(1))
        pass
    elif n - sum(coun) == 1:
        for i in range(n):
            if deg[i] > 2:
                # print('Yes')
                pass
                # print(deg[i])
                pass
                for j in range(n):
                    if deg[j] == 1:
                        # print(i + 1, j + 1)
                        pass
                return
        # print('No')
        pass

    else:
        # print('No')
        pass
if __name__ == "__main__":
    # example deterministic call
    main(10)