def gen(temp, i, s, k, outs):
    if i == k:
        j = ''
        for o in range(k):
            if temp[o] == 1:
                j += s[o]
            else:
                j += '_'
        outs.add(j)
        return
    temp[i] = 1
    gen(temp, i + 1, s, k, outs)
    temp[i] = -1
    gen(temp, i + 1, s, k, outs)


class Graph:
    def __init__(self, vertices):
        from collections import defaultdict
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if visited[neighbour] is False:
                if self.isCyclicUtil(neighbour, visited, recStack) is True:
                    return True
            elif recStack[neighbour] is True:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] is False:
                if self.isCyclicUtil(node, visited, recStack) is True:
                    return True
        return False

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)
        stack = stack[::-1]
        print("yes")
        out = []
        for i in stack:
            out.append(str(i + 1))
        print(" ".join(out))


def main(n):
    # Map n to parameters of the original problem
    # Choose number of patterns, string length k, and number of queries m
    if n < 1:
        n = 1
    k = 4
    num_patterns = n
    m = n

    # Generate pattern strings of length k deterministically
    # Characters: 'a' + (i % 3)
    all_patterns = []
    patterns = {}
    for i in range(num_patterns):
        s = []
        x = i
        for pos in range(k):
            ch = chr(ord('a') + (x % 3))
            s.append(ch)
            x //= 3
        s = "".join(s)
        all_patterns.append(s)
        patterns[s] = i

    dg = Graph(num_patterns)

    # Generate m queries deterministically
    # For query index q:
    #   pattern index mt = q % num_patterns
    #   string s is derived from all_patterns[mt] with a deterministic mask
    for q in range(m):
        mt = q % num_patterns
        base = all_patterns[mt]
        # Build query string s by replacing some positions with other chars
        s_list = list(base)
        for pos in range(k):
            if (q + pos) % 2 == 0:
                # change character deterministically
                s_list[pos] = chr(((ord(base[pos]) - ord('a') + 1) % 3) + ord('a'))
        s = "".join(s_list)

        outs = set()
        temp = [0 for _ in range(k)]
        gen(temp, 0, s, k, outs)
        if all_patterns[mt] not in outs:
            print("no")
            return
        for pattern_str in outs:
            if pattern_str != all_patterns[mt] and pattern_str in patterns:
                dg.addEdge(mt, patterns[pattern_str])

    if dg.isCyclic():
        print("no")
    else:
        dg.topologicalSort()


if __name__ == "__main__":
    main(10)