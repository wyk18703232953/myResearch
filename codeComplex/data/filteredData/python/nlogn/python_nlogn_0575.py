import random

class DFS:
    def __init__(self):
        self.G = []
        self.leave_tree = []

    def build_from_parents(self, parents):
        k = len(parents) + 1  # number of nodes
        self.G = [[] for _ in range(k)]
        for i, p in enumerate(parents):
            self.G[p].append(i + 1)

        self.leave_tree = [0] * k
        # DP from bottom to top (nodes are 0..k-1, root is 0)
        for i in range(k - 1, -1, -1):
            if len(self.G[i]) == 0:
                self.leave_tree[i] = 1
            else:
                for j in self.G[i]:
                    self.leave_tree[i] += self.leave_tree[j]
        self.leave_tree.sort()
        return self.leave_tree


def main(n):
    """
    n: number of nodes in the tree (same meaning as original 'k').
       n >= 1
    Generates a random rooted tree with n nodes (0 as root),
    runs the same logic as the original program and prints the result.
    """
    if n <= 1:
        print(n)
        return

    # Generate a random tree: for nodes 1..n-1 choose a parent in [0..i-1]
    parents = [random.randint(0, i - 1) for i in range(1, n)]

    dfs = DFS()
    res = dfs.build_from_parents(parents)
    print(*res)


if __name__ == "__main__":
    # Example run with n=10; in actual use, call main(n) with desired size.
    main(10)