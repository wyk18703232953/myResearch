def main(n):
    from collections import deque

    if n < 1:
        return

    # Deterministic tree generation: a simple path 1-2-3-...-n
    g = {}
    for i in range(1, n):
        a, b = i, i + 1
        g.setdefault(a, set()).add(b)
        g.setdefault(b, set()).add(a)

    # Deterministic sequence a:
    # For time-complexity stress, use 1..n (valid BFS order for this path tree)
    a = [i for i in range(1, n + 1)]

    ans = True
    if n > 1 and a[0] == 1:
        q = deque()
        m = [0] * (n + 1)
        q.append(1)
        m[1] = 1
        right = 1
        while len(q) > 0 and ans:
            first = q.popleft()
            cnt = 0
            for v in g[first]:
                if m[v] == 0:
                    cnt += 1
            for i in range(right, right + cnt):
                if i >= n:
                    ans = False
                    break
                if m[a[i]] == 0 and a[i] in g[first]:
                    m[a[i]] = 1
                    q.append(a[i])

                else:
                    ans = False
                    break
            right += cnt

    else:
        ans = (n >= 1 and a[0] == 1)

    if ans:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(10)