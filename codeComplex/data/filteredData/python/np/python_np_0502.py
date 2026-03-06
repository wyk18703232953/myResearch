import collections, functools, heapq, bisect, math

def binary(s):
    ans = set()
    for i in range(2**len(s)):
        x = []
        for j in range(len(s)):
            if (i >> j) & 1:
                x.append(s[j])
            else:
                x.append('_')
        ans.add(''.join(x))
    return ans

seen = set()
visited = set()
ans = []

def dfs(i, graph, n):
    visited.add(i)
    seen.add(i)
    for j in graph[i]:
        if j in visited:
            return True
        if j in seen:
            continue
        if dfs(j, graph, n):
            return True
    ans.append(str(i))
    visited.remove(i)
    return False

def topo(graph, n):
    seen.clear()
    for i in range(1, n + 1):
        if i in seen:
            continue
        if dfs(i, graph, n):
            return False
    return True

mod = 10**9 + 7

def generate_input(n):
    # Scale:
    # n: number of nodes
    # m: number of constraints ~ n
    # k is unused in original logic, keep deterministic
    if n < 1:
        n = 1
    m = n
    k = 1

    # generate d: id -> string pattern of length L
    # L chosen so that 2^L is manageable; use L = min(10, max(1, n.bit_length()))
    L = min(10, max(1, n.bit_length()))
    d = {}
    dop = {}
    for i in range(1, n + 1):
        # deterministic pattern based on i
        # characters from 'a'.., '_' avoiding randomness
        s_chars = []
        for p in range(L):
            # alternate between letters and '_'
            if ((i >> p) & 1) == 1:
                s_chars.append(chr(ord('a') + (i + p) % 3))
            else:
                s_chars.append('_')
        s = ''.join(s_chars)
        d[i] = s
        dop[s] = i

    # generate m constraints
    constraints = []
    for idx in range(m):
        ind = (idx % n) + 1
        base = d[ind]
        # modify base deterministically to create pattern s0
        # flip some positions to '_' or to another letter
        s0_chars = list(base)
        for p in range(L):
            if (idx + p) % 3 == 0:
                s0_chars[p] = '_'
            elif (idx + p) % 3 == 1:
                s0_chars[p] = base[p]
            else:
                s0_chars[p] = chr(ord('a') + (idx + p) % 3)
        s0 = ''.join(s0_chars)
        constraints.append((s0, ind))

    return n, m, k, d, dop, constraints

def main(n):
    global ans, visited, seen
    n, m, k, d, dop, constraints = generate_input(n)

    graph = collections.defaultdict(list)
    for s0, ind in constraints:
        visited.clear()
        ans = []
        sset = binary(s0)
        if d[ind] not in sset:
            print('NO')
            return
        for pattern in sset:
            if pattern in dop and dop[pattern] != ind:
                graph[dop[pattern]].append(ind)
    ans = []
    visited.clear()
    if topo(graph, n):
        print('YES')
        print(' '.join(ans))
    else:
        print('NO')

if __name__ == "__main__":
    main(8)