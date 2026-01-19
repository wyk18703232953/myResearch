import os
from io import BytesIO, IOBase
from collections import defaultdict

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = False
        self.write = None
    def read(self):
        return self.buffer.read()
    def readline(self):
        return self.buffer.readline()
    def flush(self):
        pass

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: None
        self.read = lambda: ""
        self.readline = lambda: ""

def toposort(graph):
    res = []
    found = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            res.append(1 + (~node))
        elif not found[node]:
            found[node] = 1
            stack.append(~node)
            stack.extend(graph[node])
    for node in res:
        node -= 1
        if any(found[nei] for nei in graph[node]):
            print("NO")
            return
        found[node] = 0
    print("YES")
    print(*res[::-1])

def main(n):
    if n < 1:
        n = 1
    k = max(1, n % 10)
    patterns = []
    pos = {}
    for i in range(n):
        s = []
        x = (i + 1) % (k + 1)
        if x == 0:
            x = 1
        for j in range(k):
            ch = chr(ord('a') + ((i + j + x) % 3))
            s.append(ch)
        p = "".join(s)
        patterns.append(p)
        pos[p] = i
    patterns_set = set(patterns)
    matches = [[] for _ in range(n)]
    m = n
    chk = True
    for idx in range(m):
        s = patterns[idx % n]
        mt = idx % n
        if chk:
            chk = False
            for mask in range(1 << k):
                tmp_chars = []
                for j in range(k):
                    if mask & (1 << j):
                        tmp_chars.append('_')
                    else:
                        tmp_chars.append(s[j])
                tmp = "".join(tmp_chars)
                if tmp in patterns_set:
                    if mt == pos[tmp]:
                        chk = True
                    else:
                        matches[mt].append(pos[tmp])
    if not chk:
        print("NO")
    else:
        toposort(matches)

if __name__ == "__main__":
    main(10)