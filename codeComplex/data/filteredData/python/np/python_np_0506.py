import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache

int1 = lambda x: int(x) - 1
def aj_from_list(data, idx):
    return list(map(int, data[idx].split()))

def list3d(a, b, c, d): 
    return [[[d] * c for j in range(b)] for i in range(a)]

def Y(c):  
    print(["NO","YES"][c])

def y(c):  
    print(["no","yes"][c])

def Yy(c):  
    print(["No","Yes"][c])

def solve_from_generated(lines):
    it = iter(lines)
    def next_line():
        return next(it)

    first = list(map(int, next_line().split()))
    n, m, k = first
    G = defaultdict(list)

    def addEdge(a,b):
        G[a].append(b)

    def Kahn(N):
        in_degree = [0]*(N+1)
        for i in G.keys():
            for j in G[i]:
                in_degree[j] += 1
        queue = deque()
        for i in range(1,N+1):
            if in_degree[i] == 0:
                queue.append(i)
        cnt =0
        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)
            for i in G.get(u,[]):
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
            cnt += 1
        if cnt != N:
            Y(0)
            return
        else:
            Y(1)
            print(*top_order)

    mark= {}
    for i in range(n):
        s = next_line().rstrip('\n')
        mark[s] = i+1

    B = []
    for i in range(2**k):
        f = bin(i)[2:]
        f = '0'*(k - len(f)) + f
        B.append(f)

    for _ in range(m):
        line = next_line().split()
        s = line[0]
        mt = int(line[1])
        st = set()
        for j in B:
            ss = ['']*k
            for l in range(k):
                if j[l] == '1':
                    ss[l] = s[l]
                else:
                    ss[l] = '_'
            ss = "".join(ss)
            if ss in mark:
                st.add(mark[ss])
        if mt not in st:
            Y(0)
            return
        st.discard(mt)
        for j in st:
            addEdge(mt,j)
    Kahn(n)

def main(n):
    # Interpret n as the number of patterns/vertices.
    # We set k (string length) as max(1, n % 10) to keep 2**k reasonable.
    # We set m (constraints) proportional to n.
    if n <= 0:
        return
    k = max(1, n % 10)
    m = max(1, n)  # one constraint per vertex scale

    # Generate n distinct pattern strings of length k using deterministic cycling over alphabet.
    alphabet = ['a','b','c','d']
    patterns = []
    for i in range(n):
        s_chars = []
        for pos in range(k):
            s_chars.append(alphabet[(i + pos) % len(alphabet)])
        patterns.append(''.join(s_chars))

    # Build mark mapping via the program logic: strings are keys, indices 1..n are values.
    # For constraints, we ensure at least one valid index mt belongs to each pattern's match set.
    # Simplest deterministic scheme: use the pattern itself and mt = its index, which will always be among matches.
    lines = []
    lines.append(f"{n} {m} {k}")
    for s in patterns:
        lines.append(s)

    # For constraints we cycle through the patterns and use their own index as mt.
    # Also to create some edges, we sometimes choose mt that is earlier index but pattern still compatible.
    for i in range(m):
        idx = (i % n)  # 0-based
        s = patterns[idx]
        mt = idx + 1   # 1-based
        lines.append(f"{s} {mt}")

    solve_from_generated(lines)

if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(10)