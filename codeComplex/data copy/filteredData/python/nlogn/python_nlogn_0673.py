def find_loop(g, w, k, n):
    visited = [False] * n
    visited_int = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        visited_int[i] = True
        while stack:
            if not stack[-1]:
                stack.pop()
                visited_int[path[-1]] = False
                path.pop()
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited_int[nxt]:
                return True
            if visited[nxt]:
                continue
            visited[nxt] = True
            visited_int[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)
    return False


def top_sort(g, w, k, n):
    visited = [False] * n
    order = [-1] * n
    cnt = 0
    for i in range(n):
        if visited[i]:
            continue
        stack = [g[i][:]]
        path = [i]
        visited[i] = True
        while stack:
            if not stack[-1]:
                order[path[-1]] = cnt
                path.pop()
                stack.pop()
                cnt += 1
                continue
            nxt = stack[-1][-1]
            stack[-1].pop()
            if w[(path[-1], nxt)] <= k:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = True
            stack.append(g[nxt][:])
            path.append(nxt)

    to_reverse = []
    for a, b in w.items():
        if b > k:
            continue
        if order[a[0]] < order[a[1]]:
            to_reverse.append(a)
    return to_reverse


def main(n):
    if n < 2:
        n = 2
    m = n * 2
    w = {}
    g = [[] for _ in range(n)]
    w_tmp = {}
    kk = [0]
    edge_index = 1
    for i in range(n - 1):
        u = i
        v = i + 1
        c = (i * 3) % (n + 5) + 1
        g[u].append(v)
        key = (u, v)
        if key in w:
            w[key] = max(w[key], c)

        else:
            w[key] = c
        if key in w_tmp:
            w_tmp[key].append(str(edge_index))

        else:
            w_tmp[key] = [str(edge_index)]
        kk.append(c)
        edge_index += 1
    for i in range(n):
        u = i
        v = (i + 2) % n
        c = (i * 7) % (n + 7) + 1
        g[u].append(v)
        key = (u, v)
        if key in w:
            w[key] = max(w[key], c)

        else:
            w[key] = c
        if key in w_tmp:
            w_tmp[key].append(str(edge_index))

        else:
            w_tmp[key] = [str(edge_index)]
        kk.append(c)
        edge_index += 1

    kk.sort()
    l, r = 0, len(kk)
    if not find_loop(g, w, kk[l], n):
        # print(0, 0)
        pass
        # print()
        pass
        return
    if find_loop(g, w, kk[-1], n):
        kkk = kk[-1]

    else:
        while l + 1 != r:
            m_mid = (l + r) // 2
            if find_loop(g, w, kk[m_mid], n):
                l = m_mid

            else:
                r = m_mid
        if l + 1 < len(kk):
            kkk = kk[l + 1]

        else:
            kkk = kk[-1]

    to_reverse = top_sort(g, w, kkk, n)
    num = 0
    s = []
    for t in to_reverse:
        num += len(w_tmp[t])
        s.extend(w_tmp[t])

    # print(kkk, num)
    pass
    # print(" ".join(s))
    pass
if __name__ == "__main__":
    main(10)