import sys
from collections import deque

def main(n):
    # Deterministically generate n, d, k from input scale n
    # Ensure d < n so the original logic can proceed meaningfully
    if n < 3:
        n_val = 3

    else:
        n_val = n

    # Define d as about half of n, but at least 1 and less than n
    d = max(1, min(n_val - 1, n_val // 2))
    # Define k as at least 2, and not too small compared to d
    k = max(2, d // 2 + 1)

    n_local = n_val

    if d >= n_local:
        # print("NO")
        pass
        return

    graph = [[] for _ in range(n_local + 1)]

    for i in range(1, d + 2):
        graph[i].append(min(i - 1, d + 1 - i))

    for i in range(1, d + 1):
        graph[i].append(i + 1)
        graph[i + 1].append(i)

    deg = [0] * (n_local + 1)
    deg[1] = 1
    deg[d + 1] = 1
    for i in range(2, d + 1):
        deg[i] = 2

    for x in deg:
        if x > k:
            # print("NO")
            pass
            return

    p = d + 2
    for i in range(1, d + 2):
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            while graph[x][0] > 0 and deg[x] < k and p <= n_local:
                graph[x].append(p)
                deg[x] += 1
                graph[p].append(graph[x][0] - 1)
                graph[p].append(x)
                deg[p] += 1
                q.append(p)
                p += 1

    if p <= n_local:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        vis = [-1] * (n_local + 1)
        for i in range(1, d + 2):
            if vis[i] == -1:
                q = deque()
                q.append(i)
                while q:
                    x = q.popleft()
                    vis[x] = 1
                    for j in range(1, len(graph[x])):
                        if vis[graph[x][j]] == -1:
                            # print(x, graph[x][j])
                            pass
                            q.append(graph[x][j])

if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)