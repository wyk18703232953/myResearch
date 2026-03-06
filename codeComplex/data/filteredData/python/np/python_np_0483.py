import sys
from enum import Enum

class flag(Enum):
    UNVISITED = -1
    EXPLORED = -2
    VISITED = -3

def match(p, s):
    for i in range(len(p)):
        if p[i] != "_" and p[i] != s[i]:
            return False
    return True

def cycleCheck(u):
    global AL
    global dfs_num
    global dfs_parent
    global sol

    dfs_num[u] = flag.EXPLORED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            dfs_parent[v] = u
            cycleCheck(v)
        elif dfs_num[v] == flag.EXPLORED.value:
            sol = False
    dfs_num[u] = flag.VISITED.value

def toposort(u):
    global AL
    global dfs_num
    global ts

    dfs_num[u] = flag.VISITED.value
    for v in AL[u]:
        if dfs_num[v] == flag.UNVISITED.value:
            toposort(v)
    ts.append(u)

def generate_data(n):
    # n: number of patterns
    # m: number of constraints, here set equal to n for scalability
    # k is unused in original logic; keep it as 0
    k = 0
    m = n

    # Generate patterns pa and associated structures
    # Patterns are strings of length L = 5 over {'a', 'b', '_'}
    # Deterministic construction: mostly 'a', with some '_' and 'b'
    L = 5
    pa = []
    pd = {}
    ps = set()
    for i in range(n):
        s = []
        for j in range(L):
            r = (i + j) % 3
            if r == 0:
                s.append('a')
            elif r == 1:
                s.append('_')
            else:
                s.append('b')
        p = ''.join(s)
        pa.append(p)
        idx = i + 1
        pd[p] = idx
        ps.add(p)

    # Generate m constraints (s, fn)
    # For each i, generate one string s of length L over {'a','b'}
    # and map it to fn = (i % n) + 1
    constraints = []
    for i in range(m):
        s_chars = []
        for j in range(L):
            if (i + j) % 2 == 0:
                s_chars.append('a')
            else:
                s_chars.append('b')
        s = ''.join(s_chars)
        fn = (i % n) + 1
        constraints.append((s, fn))

    return n, m, k, pa, pd, ps, constraints

def main(n):
    global AL
    global dfs_num
    global dfs_parent
    global sol
    global ts

    n, m, k, pa, pd, ps, constraints = generate_data(n)

    sol = True
    AL = [[] for _ in range(n)]

    for (s, fn) in constraints:
        if not match(pa[fn-1], s):
            sol = False

        mm = [""]
        for ch in s:
            mm = list(map(lambda x: x + "_", mm)) + list(map(lambda x: x + ch, mm))
        for pat in mm:
            if pat in ps:
                if pd[pat] != fn:
                    AL[fn-1].append(pd[pat]-1)

    try:
        if not sol:
            print("NO")
        else:
            dfs_num = [flag.UNVISITED.value] * n
            dfs_parent = [-1] * n
            for u in range(n):
                if dfs_num[u] == flag.UNVISITED.value:
                    cycleCheck(u)
            if not sol:
                print("NO")
            else:
                dfs_num = [flag.UNVISITED.value] * n
                ts = []
                for u in range(n):
                    if dfs_num[u] == flag.UNVISITED.value:
                        toposort(u)
                ts = ts[::-1]
                print("YES")
                print(' '.join(map(lambda x: str(x+1), ts)))
    except:
        print("NO")

if __name__ == "__main__":
    main(10)