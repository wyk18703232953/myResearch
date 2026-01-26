def main(n):
    # n: number of nodes in the tree
    if n < 1:
        return

    # Deterministically construct a tree and a traversal sequence a
    # Here we use a simple chain tree: 1-2-3-...-n
    g = dict()
    for i in range(1, n):
        a_node = i
        b_node = i + 1
        g.setdefault(a_node, set()).add(b_node)
        g.setdefault(b_node, set()).add(a_node)

    # Deterministically construct the sequence a of length n
    # Use BFS order (which is just [1,2,...,n] for a chain starting at 1)
    a = [i for i in range(1, n + 1)]

    from collections import deque

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
                if i >= len(a):
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
        ans = a[0] == 1

    if ans:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)