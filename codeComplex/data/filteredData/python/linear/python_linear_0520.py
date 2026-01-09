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
    # Generate a simple deterministic tree:
    # Node 0 connected to all others (star tree)
    a = [set() for _ in range(n)]
    for v in range(1, n):
        a[0].add(v)
        a[v].add(0)
    # Deterministic BFS-like sequence: 0,1,2,...,n-1
    s = list(range(n))
    return a, s

def main(n):
    if n <= 0:
        return
    a, s = generate_tree_and_sequence(n)
    res = solve(a, s)
    # print("Yes" if res else "No")
    pass
if __name__ == "__main__":
    main(10)