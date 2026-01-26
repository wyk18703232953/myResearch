class DFS:
    def __init__(self):
        self.G = []
        self.leave_tree = []

    def run(self, k, parent_list):
        if k > 1:
            graph = [p for p in parent_list]
            self.G = [[] for _ in range(len(graph) + 1)]
            for i in range(len(graph)):
                self.G[graph[i]].append(i + 1)
            self.visited = [0] * k
            self.leave_tree = [0] * k
            for i in range(k - 1, -1, -1):
                if len(self.G[i]) == 0:
                    self.leave_tree[i] = 1

                else:
                    for j in self.G[i]:
                        self.leave_tree[i] += self.leave_tree[j]
            self.leave_tree.sort()
            return self.leave_tree

        else:
            return [k]


def main(n):
    if n <= 0:
        return []
    k = n
    if k == 1:
        parent_list = []

    else:
        parent_list = [(i - 1) // 2 for i in range(1, k)]
    dfs = DFS()
    return dfs.run(k, parent_list)


if __name__ == "__main__":
    result = main(10)
    # print(*result)
    pass