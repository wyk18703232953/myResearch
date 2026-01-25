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

def build_tree(n):
    G = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        parent = i // 2
        G[parent].append(i)
        G[i].append(parent)
    return G

def main(n):
    if n < 1:
        print(0)
        return
    G = build_tree(n)
    ans = bfs(1, n, G)
    print(ans)

if __name__ == "__main__":
    main(10)