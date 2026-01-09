def main(n):
    # Interpret n as the number of nodes.
    # Deterministically derive parameters d and k from n.
    if n < 2:
        # For n < 2, the original algorithm is either trivial or invalid.
        # To keep behavior deterministic and simple, just print NO.
        # print("NO")
        pass
        return

    # Define d in [1, n-1] and k >= 1 deterministically
    d = max(1, (n - 1) // 2)
    k = max(1, n // 3)

    if d + 1 > n:
        # print("NO")
        pass
        return

    ans = []
    dist = [0] * n
    deg = [0] * n
    for i in range(d + 1):
        if i == 0 or i == d:
            deg[i] = 1

        else:
            deg[i] = 2
        if i != d:
            ans.append((i + 1, i + 2))
        dist[i] = max(i, d - i)

    for i in range(n):
        if deg[i] > k:
            # print("NO")
            pass
            return

    from collections import deque
    q = deque(list(range(d + 1)))
    cur = d + 1
    while q and cur < n:
        v = q.popleft()
        if dist[v] < d and deg[v] < k:
            deg[v] += 1
            dist[cur] = dist[v] + 1
            deg[cur] = 1
            ans.append((v + 1, cur + 1))
            q.append(v)
            q.append(cur)
            cur += 1

        else:
            continue

    if cur != n:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        for u, v in ans:
            # print(u, v)
            pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)