import sys

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


def build_graph(n):
    m = n * 2
    g = [[] for _ in range(n)]
    w = {}
    w_tmp = {}
    kk = [0]
    idx = 1
    for i in range(n):
        u = i
        v = (i + 1) % n
        c = (i * 3 + 7) % (n + 5) + 1
        g[u].append(v)
        if (u, v) in w:
            w[(u, v)] = max(w[(u, v)], c)
        else:
            w[(u, v)] = c
        if (u, v) in w_tmp:
            w_tmp[(u, v)].append(str(idx))
        else:
            w_tmp[(u, v)] = [str(idx)]
        kk.append(c)
        idx += 1
    for i in range(n):
        u = i
        v = (i + 2) % n
        c = (i * 5 + 11) % (n + 7) + 1
        g[u].append(v)
        if (u, v) in w:
            w[(u, v)] = max(w[(u, v)], c)
        else:
            w[(u, v)] = c
        if (u, v) in w_tmp:
            w_tmp[(u, v)].append(str(idx))
        else:
            w_tmp[(u, v)] = [str(idx)]
        kk.append(c)
        idx += 1
    kk.sort()
    return g, w, w_tmp, kk


def main(n):
    if n <= 0:
        return
    g, w, w_tmp, kk = build_graph(n)
    l, r = 0, len(kk)
    if not find_loop(g, w, kk[l], n):
        print(0, 0)
        return
    if find_loop(g, w, kk[-1], n):
        kkk = kk[-1]
    else:
        while l + 1 != r:
            m = (l + r) // 2
            if find_loop(g, w, kk[m], n):
                l = m
            else:
                r = m
        kkk = kk[l + 1]

    to_reverse = top_sort(g, w, kkk, n)
    num = 0
    s = []
    for t in to_reverse:
        num += len(w_tmp[t])
        s.extend(w_tmp[t])

    print(kkk, num)
    if s:
        print(" ".join(s))
    else:
        print()


if __name__ == "__main__":
    main(10)