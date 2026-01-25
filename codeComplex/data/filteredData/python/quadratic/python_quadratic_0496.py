def main(n):
    if n <= 1:
        print(1)
        return

    # 构造一个确定性的父节点数组 p，表示一棵树的父节点关系（1 为根）
    # p 的长度为 n-1，p[i] 表示节点 i+2 的父节点
    # 这里构造一棵简单但非退化的树：每个节点的父亲为 i//2+1（模仿完全二叉树）
    p = [(i // 2) + 1 for i in range(1, n)]

    children = [[] for _ in range(n)]
    for i in range(n - 1):
        children[p[i] - 1].append(i + 1)

    layers = [1] + [0] * (n - 1)
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
    print(out)


if __name__ == "__main__":
    main(10)