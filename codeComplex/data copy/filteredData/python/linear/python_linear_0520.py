from collections import deque

def removeUsed(adj, used):
    to_remove = []
    for s in adj:
        if used[s]:
            to_remove.append(s)
    for s in to_remove:
        adj.remove(s)

def solve(a, s):
    if s[0] != 0:
        return False
    q = deque()
    q.append(0)
    i, n, cur = 1, len(a), -1
    used = [False] * n
    used[0] = True
    while i < n:
        if cur == -1:
            if not q:
                return False
            cur = q.popleft()
            removeUsed(a[cur], used)
        if not a[cur]:
            cur = -1
            continue
        cur_s = s[i]
        i += 1
        if cur_s not in a[cur]:
            return False
        a[cur].remove(cur_s)
        q.append(cur_s)
        used[cur_s] = True
    return True

def generate_tree_and_sequence(n):
    if n <= 0:
        return [], []
    # Build a simple deterministic tree: a line 1-2-3-...-n
    a = [set() for _ in range(n)]
    for i in range(1, n):
        u = i - 1
        v = i
        a[u].add(v)
        a[v].add(u)
    # Deterministic BFS-like sequence that is valid for the line tree:
    # s = [0,1,2,...,n-1]
    s = list(range(n))
    return a, s

def main(n):
    a, s = generate_tree_and_sequence(n)
    result = solve(a, s)
    # print("Yes" if result else "No")
    pass
if __name__ == "__main__":
    main(10)