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

def generate_input(n):
    # Deterministically generate:
    # n: number of patterns
    # m: number of constraints
    # k: unused in original code, keep as 0
    # patterns: strings of 'a','b','_' length = (n % 3) + 1
    # constraints: m lines (s, fn)
    if n <= 0:
        n = 1
    L = n % 3 + 1
    alphabet = ["a", "b", "_"]
    patterns = []
    for i in range(n):
        pattern = "".join(alphabet[(i + j) % 3] for j in range(L))
        patterns.append(pattern)
    ps = set(patterns)
    pd = {p: i + 1 for i, p in enumerate(patterns)}

    # Build m constraints deterministically.
    # For each pattern index i, create one constraint with s being pattern
    # rotated and fn = (i % n) + 1
    constraints = []
    for i in range(n):
        p = patterns[i]
        rot = p[1:] + p[0] if len(p) > 1 else p
        fn = (i % n) + 1
        constraints.append((rot, fn))

    m = len(constraints)
    k = 0
    return n, m, k, pd, ps, patterns, constraints

def core_logic(n, m, k, pd, ps, pa, constraints):
    global AL
    global dfs_num
    global dfs_parent
    global sol
    global ts

    sol = True
    AL = [[] for _ in range(n)]

    for s, fn in constraints:
        if not match(pa[fn-1], s):
            sol = False

        mm = [""]
        for ch in s:
            mm = list(map(lambda x: x + "_", mm)) + list(map(lambda x: x + ch, mm))
        for i in mm:
            if i in ps:
                if pd[i] != fn:
                    AL[fn-1].append(pd[i]-1)

    try:
        if not sol:
            return "NO"
        dfs_num = [flag.UNVISITED.value] * n
        dfs_parent = [-1] * n
        for u in range(n):
            if dfs_num[u] == flag.UNVISITED.value:
                cycleCheck(u)
        if not sol:
            return "NO"
        dfs_num = [flag.UNVISITED.value] * n
        ts = []
        for u in range(n):
            if dfs_num[u] == flag.UNVISITED.value:
                toposort(u)
        ts = ts[::-1]
        return "YES\n" + " ".join(str(x + 1) for x in ts)
    except:
        return "NO"

def main(n):
    n_gen, m, k, pd, ps, pa, constraints = generate_input(n)
    result = core_logic(n_gen, m, k, pd, ps, pa, constraints)
    print(result)

if __name__ == "__main__":
    main(10)