from collections import defaultdict
from collections import deque

class graph:
    def __init__(self):
        self.g = defaultdict(list)
    def addedge(self, u, v):
        self.g[u].append(v)

def router(values):
    gr = graph()
    for i in range(len(values)):
        gr.addedge(values[i], i + 2)
    return gr.g

def isleaf(node, gr):
    if len(gr[node]) == 0:
        return True
    return False

def christmas(gr, start, visited):
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
    # Deterministic construction of a parent array of length n-1
    # Ensures values[i] is in [1, i+1] so that the resulting graph is connected
    values = []
    for i in range(n - 1):
        parent = (i % (i + 1)) + 1
        values.append(parent)
    return values

def main(n):
    if n <= 1:
        # For n <= 1, construct minimal structures consistent with the original program
        values = []
        gr = router(values)
        visited = [False] * (n + 2)
        result = christmas(gr, 1, visited)
        print(result)
        return
    values = generate_values(n)
    gr = router(values)
    visited = [False] * (n + 2)
    result = christmas(gr, 1, visited)
    print(result)

if __name__ == "__main__":
    main(10)