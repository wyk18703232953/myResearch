from collections import deque

def main(n):
    # 构造一棵以 1 为根的链式树：1-2-3-...-n
    g = {}
    for i in range(1, n + 1):
        g.setdefault(i, set())
    for i in range(2, n + 1):
        a, b = i - 1, i
        g[a].add(b)
        g[b].add(a)

    # 确定性构造访问序列 a
    # 这里选用从 1 到 n 的顺序，始终是合法的 BFS 序
    if n <= 0:
        a = []

    else:
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
                if m[a[i]] == 0 and a[i] in g[first]:
                    m[a[i]] = 1
                    q.append(a[i])

                else:
                    ans = False
                    break
            right += cnt

    else:
        ans = (len(a) > 0 and a[0] == 1)

    if ans:
        # print("Yes")
        pass

    else:
        # print("No")
        pass
if __name__ == "__main__":
    main(10)