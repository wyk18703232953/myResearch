def main(n):
    if n < 1:
        # print("")
        pass
        return

    # Deterministic generation of arr (parent array for nodes 2..n)
    # arr[j] in [1, j+1], using a simple pattern
    arr = [i % (i + 1) + 1 for i in range(n - 1)]

    children = [[] for _ in range(n + 1)]
    for i, j in enumerate(arr):
        node = i + 2
        if 1 < node <= n:
            if j <= n:
                children[j].append(node)

    leaves = [0] * (n + 1)

    for i in range(n, 0, -1):
        if not children[i]:
            leaves[i] = 1

        else:
            leaves[i] = sum(leaves[j] for j in children[i])

    # print(' '.join(map(str, sorted(leaves[1:]))))
    pass
if __name__ == "__main__":
    main(10)