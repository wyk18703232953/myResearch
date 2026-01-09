def main(n):
    # Generate a deterministic tree with n nodes
    # For simplicity and determinism, create a chain 1-2-3-...-n when n >= 2
    # and a single node when n == 1
    d = {}
    if n == 1:
        d[1] = []

    else:
        for i in range(1, n):
            u, v = i, i + 1
            d.setdefault(u, []).append(v)
            d.setdefault(v, []).append(u)

    # Original logic
    node = 1
    for key in d:
        if len(d[key]) > len(d[node]):
            node = key
    ans = []
    visited = [0] * n
    visited[node - 1] = 1
    for c in d[node]:
        while True:
            visited[c - 1] = 1
            if len(d[c]) == 1:
                ans.append([node, c])
                break
            for child in d[c]:
                if visited[child - 1] != 1:
                    c = child
                    break

            else:
                break
    if sum(visited) == n:
        # print("Yes")
        pass
        # print(len(ans))
        pass
        for c in ans:
            # print(*c)
            pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(5)