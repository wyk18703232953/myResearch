from collections import deque

def bfs(s, n, G):
    q = deque()
    q.append(s)
    dist = [-1] * (n + 1)
    dist[s] = 0
    p = []
    parent = [1] * (n + 1)
    ok = [0] * (n + 1)
    while q:
        i = q.popleft()
        d = dist[i]
        if d < 3:
            ok[i] = 1
        p.append(i)
        for j in G[i]:
            if dist[j] == -1:
                q.append(j)
                dist[j] = d + 1
                parent[j] = i
    ans = 0
    while p:
        i = p.pop()
        j = parent[i]
        if not ok[i]:
            ok[j] = 1
            ans += 1
            for k in G[j]:
                ok[k] = 1
    return ans

def generate_tree(n):
    # Deterministic tree: for i in 2..n, connect i with i//2
    G = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        u = i
        v = i // 2
        G[u].append(v)
        G[v].append(u)
    return G

def main(n):
    if n < 1:
        return 0
    G = generate_tree(n)
    ans = bfs(1, n, G)
    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    main(10)