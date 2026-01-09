def main(n):
    from collections import deque

    if n < 1:
        return

    # 构造一棵确定性的树（链式：1-2-3-...-n）
    g = {}
    for i in range(1, n + 1):
        g.setdefault(i, set())
    for i in range(1, n):
        a = i
        b = i + 1
        g[a].add(b)
        g[b].add(a)

    # 构造一个确定性的遍历序列 a
    # 这里使用从 1 到 n 的顺序遍历（合法 BFS 序）
    a = list(range(1, n + 1))

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
    main(10)