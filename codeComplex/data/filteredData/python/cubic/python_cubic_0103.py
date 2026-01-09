import sys

class Graph:
    verticies = {}
    nodesCount = 0

    class Vertex:
        def __init__(self, label, endPoint=None):
            self.label = label
            self.edges = []
            self.visitedToken = 0
            self.endPoint = endPoint

    class Edge:
        residual = None

        def __init__(self, from_, to_, isResidual, maxCapacity):
            self.from_ = from_
            self.to_ = to_
            self.isResidual = isResidual
            self.capacity = maxCapacity
            self.flow = 0

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


def generate_data(n):
    if n < 2:
        n = 2
    m = n
    vv = [i + 1 for i in range(n)]
    edges = []
    for i in range(1, m + 1):
        a = (i % n) + 1 if n > 1 else 1
        b = ((i * 2) % n) + 1 if n > 1 else 1
        c = i
        edges.append((a, b, c))
    return n, m, vv, edges


def main(n):
    g = Graph()
    n_nodes, m, vv, edges = generate_data(n)

    for i in range(n_nodes + m + 2):
        g.addVertex(i)

    for i, v in enumerate(vv):
        g.addEdge(m + i + 1, n_nodes + m + 1, v)

    s = 0

    for i in range(1, m + 1):
        a, b, c = edges[i - 1]
        s += c
        g.addEdge(0, i, c)
        g.addEdge(i, a + m, c)
        g.addEdge(i, b + m, c)

    result = s - g.maxFlow(0, n_nodes + m + 1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)