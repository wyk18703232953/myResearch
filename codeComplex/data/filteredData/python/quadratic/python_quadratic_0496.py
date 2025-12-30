import random

def main(n):
    # 生成一棵以 0 为根的随机树的父节点数组 p（长度 n-1，节点编号 1..n-1）
    # 原程序中 p[i] 是节点 i+1 的父亲（1-based），这里保持一致
    if n == 1:
        print(1)
        return

    # 随机生成一棵树：每个节点 i(1..n-1) 随机连接到 [0..i-1] 中的某个节点
    p = [random.randint(1, i) for i in range(1, n)]  # 存的是父节点编号的 1-based 形式

    children = [[] for _ in range(n)]
    for i in range(n - 1):
        # p[i] 是父节点（1-based），i+1 为子节点（0-based 节点号）
        children[p[i] - 1].append(i + 1)

    layers = [1] + [0] * (n - 1)
    layer = [0]
    num = 2
    bylayer = []
    # BFS 分层
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
    # 自底向上统计每个节点的“叶子数”之和
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
    print(out.strip())


# 示例手动调用：
# main(5)