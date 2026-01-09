def router(values):
    from collections import defaultdict
    class graph:
        def __init__(self):
            self.g = defaultdict(list)
        def addedge(self, u, v):
            self.g[u].append(v)

    gr = graph()
    for i in range(len(values)):
        gr.addedge(values[i], i + 2)
    return gr.g

def isleaf(node, gr):
    if len(gr[node]) == 0:
        return True
    return False

def christmas(gr, start, visited):
    from collections import deque
    q = deque()
    q.append(start)
    visited[start] = True
    count = 0
    while q:
        count = 0
        value = q.popleft()
        for val in gr[value]:
            if not isleaf(val, gr):
                q.append(val)
                visited[val] = True

            else:
                visited[val] = True
                count = count + 1
        if count < 3:
            return 'No'
    if count < 3:
        return 'No'
    return 'Yes'

def generate_values(n):
    # Deterministically generate parent list for a tree of size n
    # values[i] is the parent of node (i+2), ensure 1 <= parent <= i+1
    # Simple pattern: parent of node k is k//2
    # For node index in values: node = i+2, parent = (i+2)//2
    return [(i + 2) // 2 for i in range(n - 1)]

def main(n):
    if n <= 0:
        return
    if n == 1:
        gr = {1: []}
        visited = [False] * (n + 1)
        result = christmas(gr, 1, visited)
        # print(result)
        pass
        return
    values = generate_values(n)
    gr = router(values)
    visited = [False] * (n + 1)
    result = christmas(gr, 1, visited)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)