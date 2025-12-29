import sys
import random


class Graph:
    def __init__(self):
        self.verticies = {}
        self.nodesCount = 0

    class Vertex:
        def __init__(self, label, endPoint=None):
            self.label = label
            self.edges = []
            self.visitedToken = 0
            self.endPoint = endPoint

    class Edge:
        def __init__(self, from_, to_, isResidual, maxCapacity):
            self.from_ = from_
            self.to_ = to_
            self.isResidual = isResidual
            self.capacity = maxCapacity
            self.flow = 0
            self.residual = None

        def augment(self, bootleneck):
            self.flow += bootleneck
            self.residual.flow -= bootleneck

        def remainingCapacity(self):
            return self.capacity - self.flow

    def addEdge(self, from_, to_, capacity):
        from_ = self.verticies[from_]
        to_ = self.verticies[to_]
        if from_.endPoint and from_.endPoint != to_:
            from_ = from_.endPoint

        main = self.Edge(from_, to_, False, capacity)
        residual = self.Edge(to_, from_, True, 0)

        main.residual = residual
        residual.residual = main

        from_.edges.append(main)
        to_.edges.append(residual)

    def addVertex(self, label, *args):
        self.nodesCount += 1
        self.verticies[label] = self.Vertex(label)

    def maxFlow(self, f, t):
        f = self.verticies[f]
        t = self.verticies[t]
        visitedToken = 1
        flow = 0

        def dfs(node, bootleneck=sys.maxsize):
            node.visitedToken = visitedToken
            bootleneck_backup = bootleneck

            if node == t:
                return bootleneck

            for edge in node.edges:
                if edge.remainingCapacity() == 0 or edge.to_.visitedToken == visitedToken:
                    continue

                bootleneck = dfs(edge.to_, min(
                    bootleneck, edge.remainingCapacity()))
                if bootleneck:
                    edge.augment(bootleneck)
                    return bootleneck
                else:
                    bootleneck = bootleneck_backup

            return 0

        while True:
            bootleneck = dfs(f)
            if not bootleneck:
                break

            flow += bootleneck
            visitedToken += 1

        return flow


def main(n):
    """
    n: 规模参数，用于生成测试数据
       这里设定：n 为 '物品/右侧点' 的数量
       左侧点数量 m 与 n 相同（可按需修改）
    """
    random.seed(0)

    g = Graph()

    # 设定 m 与 n 相关，这里简单设为 m = n
    m = n

    # 生成右侧点的容量 vv，正整数
    # 节点索引：0 为源点，1..m 为左侧点，m+1 .. m+n 为右侧点，m+n+1 为汇点
    vv = [random.randint(1, 10) for _ in range(n)]

    # 建点：总点数 = n + m + 2 (含源点 0 和汇点 n+m+1)
    for i in range(n + m + 2):
        g.addVertex(i)

    # 右侧点连接到汇点，容量为 vv
    for i, v in enumerate(vv):
        g.addEdge(m + i + 1, n + m + 1, v)

    s = 0

    # 生成左侧点及其边：
    # 对于每个 i in [1..m]:
    #   随机选两个右侧点 a, b，随机容量 c
    for i in range(1, m + 1):
        a = random.randint(1, n)
        b = random.randint(1, n)
        c = random.randint(1, 10)
        s += c

        # 源点到左侧点
        g.addEdge(0, i, c)
        # 左侧点到两个右侧点
        g.addEdge(i, a + m, c)
        g.addEdge(i, b + m, c)

    ans = s - g.maxFlow(0, n + m + 1)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)