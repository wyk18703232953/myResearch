def main(n):
    if n <= 1:
        # Original behavior: when n == 1, directly print 1
        # print(1)
        pass
        return

    # Deterministically generate parent array p of length n-1
    # p[i] in [1, i+1], forming a rooted tree with root 1
    p = [(i % (i + 1)) + 1 for i in range(n - 1)]

    children = [[] for _ in range(n)]
    for i in range(n - 1):
        children[p[i] - 1].append(i + 1)

    layers = [0] * n
    layers[0] = 1
    layer = [0]
    num = 2
    bylayer = []
    while len(layer) > 0:
        bylayer.append(layer)
        newlayer = []
        for vert in layer:
            for child in children[vert]:
                layers[child] = num
                newlayer.append(child)
        layer = newlayer
        num += 1

    bylayer = bylayer[::-1]
    count = [0] * n
    for layer in bylayer:
        for vert in layer:
            if children[vert] == []:
                count[vert] = 1

            else:
                count[vert] = sum(count[v] for v in children[vert])

    count.sort()
    out = ""
    for guy in count:
        out += str(guy) + " "
    # print(out)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)