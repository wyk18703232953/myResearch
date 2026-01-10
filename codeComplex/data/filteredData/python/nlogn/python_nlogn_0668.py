import copy

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


def generate_graph(n):
    # Deterministic graph generation:
    # Create a directed graph where each node i has edges to (i+1) % n, (i+2) % n, ..., up to a limit.
    # Edge weights are simple functions of (u, v) and n.
    g = [[] for _ in range(n)]
    w = {}
    w_tmp = {}
    kk = [0]
    edge_index = 1

    if n <= 1:
        return g, w, w_tmp, kk

    max_out_deg = max(1, n // 3)
    for u in range(n):
        deg = min(max_out_deg, n - 1)
        for step in range(1, deg + 1):
            v = (u + step) % n
            weight = (u * 131 + v * 17 + n) % (3 * n + 7) + 1
            g[u].append(v)
            key = (u, v)
            if key in w:
                if weight > w[key]:
                    w[key] = weight
            else:
                w[key] = weight
            if key in w_tmp:
                w_tmp[key].append(str(edge_index))
            else:
                w_tmp[key] = [str(edge_index)]
            kk.append(weight)
            edge_index += 1

    kk.sort()
    return g, w, w_tmp, kk


def main(n):
    g, w, w_tmp, kk = generate_graph(n)

    if n == 0:
        print(0, 0)
        print()
        return

    l, r = 0, len(kk)
    if not find_loop(g, w, kk[l], n):
        print(0, 0)
        print()
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
    print(" ".join(s))


if __name__ == "__main__":
    main(10)