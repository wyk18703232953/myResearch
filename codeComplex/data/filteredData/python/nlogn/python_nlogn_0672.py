from collections import deque

def solve_instance(N, edges):
    table = []
    for s, t, c in edges:
        s, t = s - 1, t - 1
        table.append((s, t, c))

    def check(k):
        Lin = [0] * N
        edge = [[] for _ in range(N)]
        for s, t, c in table:
            if c > k:
                Lin[t] += 1
                edge[s].append(t)
        Haco = deque()
        ans = []
        for i in range(N):
            if Lin[i] == 0:
                ans.append(i)
                Haco.append(i)
        while Haco:
            x = Haco.pop()
            for y in edge[x]:
                Lin[y] -= 1
                if Lin[y] == 0:
                    ans.append(y)
                    Haco.append(y)
        return ans

    ma = 10**9 + 7
    mi = -1
    while ma - mi > 1:
        mid = (ma + mi) // 2
        if len(check(mid)) == N:
            ma = mid
        else:
            mi = mid
    ans = check(ma)

    dd = {}
    for i in range(N):
        dd[ans[i]] = i

    num = 0
    answer = []
    M = len(table)
    for i in range(M):
        s, t, c = table[i]
        if dd[s] > dd[t] and c <= ma:
            answer.append(i + 1)
            num += 1
    print(ma, num)
    print(' '.join(map(str, answer)))


def main(n):
    if n < 2:
        n = 2
    N = n
    M = n * 2
    edges = []
    # Deterministic construction: chain edges + cross edges with varying costs
    for i in range(1, N):
        c = (i * 3) % (10**6 + 3)
        if c == 0:
            c = i
        edges.append((i, i + 1, c))
    # Add extra edges to reach M edges
    cur = len(edges)
    a, b = 1, 3
    while cur < M:
        s = (a % N) + 1
        t = (b % N) + 1
        if s == t:
            t = (t % N) + 1
        c = (a * b + 5) % (10**6 + 3)
        if c == 0:
            c = a + b
        edges.append((s, t, c))
        a += 2
        b += 3
        cur += 1
    solve_instance(N, edges)


if __name__ == "__main__":
    main(10)