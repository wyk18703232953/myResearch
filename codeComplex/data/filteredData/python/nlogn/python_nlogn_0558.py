from collections import deque

def main(n):
    if n < 2:
        print("No")
        return

    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    l = [[] for _ in range(n + 2)]

    for i in range(2, n + 1):
        parent = i // 2
        l[parent].append(i)
        l[i].append(parent)

    bfs_order = []
    q = deque([1])
    visited_gen = [False] * (n + 2)
    visited_gen[1] = True
    while q:
        u = q.popleft()
        bfs_order.append(u)
        for v in l[u]:
            if not visited_gen[v]:
                visited_gen[v] = True
                q.append(v)

    b = deque(bfs_order)
    b.appendleft(0)
    b.popleft()

    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    s = deque([1])
    ans = "Yes"
    visited[1] = True

    while len(b) > 0 and len(s) > 0:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b:
                ans = "No"
                s.clear()
                break
            x = b.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1
            else:
                ans = "No"
                b.clear()
                break
        s.popleft()
    print(ans)

if __name__ == "__main__":
    main(10)