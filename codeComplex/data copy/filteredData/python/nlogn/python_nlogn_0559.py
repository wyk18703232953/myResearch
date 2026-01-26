def main(n):
    from collections import deque

    if n < 1:
        return

    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    l = [[] for _ in range(n + 2)]

    # Deterministic tree: path 1-2-3-...-n
    for i in range(1, n):
        a = i
        b = i + 1
        l[a].append(b)
        l[b].append(a)

    # Deterministic permutation b: [1, 2, ..., n]
    b = deque(range(1, n + 1))
    b.popleft()

    s = deque([1])
    visited[1] = True

    ok = True
    while len(b) > 0 and len(s) > 0 and ok:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b:
                ok = False
                break
            x = b.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1

            else:
                ok = False
                break
        s.popleft()

    if ok and len(b) == 0:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(10)