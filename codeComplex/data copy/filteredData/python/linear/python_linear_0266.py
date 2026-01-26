import sys


def generate_tree(n):
    if n <= 1:
        return []
    edges = []
    # create a simple path tree: 1-2-3-...-n
    for i in range(1, n):
        edges.append([i, i + 1])
    return edges


def main(n):
    # generate deterministic tree with n nodes
    if n <= 0:
        return

    deg = [0] * n
    edges = generate_tree(n)

    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    coun = [0, deg.count(1), deg.count(2)]

    if n - coun[1] == 1:
        # print(f'Yes\n{n - 1}')
        pass
        for x in edges:
            # print(*x)
            pass
    elif coun[1] + coun[2] == n:
        # print(f'Yes\n1')
        pass
        # print(deg.index(1) + 1, n - deg[::-1].index(1))
        pass
    elif n - sum(coun) == 1:
        for i in range(n):
            if deg[i] > 2:
                # print(f'Yes\n{deg[i]}')
                pass
                for j in range(n):
                    if deg[j] == 1:
                        # print(i + 1, j + 1)
                        pass
                return

    else:
        # print('No')
        pass
if __name__ == "__main__":
    # example deterministic call
    main(10)