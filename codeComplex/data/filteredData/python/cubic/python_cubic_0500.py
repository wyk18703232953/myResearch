import math

class Node:
    def __init__(self, u=math.inf, d=math.inf, l=math.inf, r=math.inf):
        self.up = u
        self.dn = d
        self.lt = l
        self.rt = r
    def __str__(self):
        return 'U:{},D:{},L:{},R:{}'.format(self.up, self.dn, self.lt, self.rt)

def build_graph(n, m):
    graph = [[Node() for _ in range(m)] for _ in range(n)]
    # horizontal weights: simple deterministic pattern
    for i in range(n):
        wts = [(i + j + 1) for j in range(m - 1)]
        for j in range(m - 1):
            graph[i][j].rt = wts[j]
            graph[i][j + 1].lt = wts[j]
    # vertical weights: another deterministic pattern
    for i in range(n - 1):
        wts = [((i + 1) * (j + 1)) for j in range(m)]
        for j in range(m):
            graph[i][j].dn = wts[j]
            graph[i + 1][j].up = wts[j]
    return graph

def solve(n_rows, n_cols, k_steps, graph):
    n = n_rows
    m = n_cols
    ans = [[math.inf for _ in range(m)] for _ in range(n)]
    if k_steps % 2:
        return [[-1 for _ in range(m)] for _ in range(n)]
    dp = [[[math.inf for _ in range(k_steps + 1)] for _ in range(m)] for _ in range(n)]

    def bfs(prsnt, stps):
        if stps == 0:
            return 0
        if dp[prsnt[0]][prsnt[1]][stps] == math.inf:
            min_cost = math.inf
            i, j = prsnt
            for x, y, c in [
                (0, 1, graph[i][j].dn),
                (1, 0, graph[i][j].rt),
                (0, -1, graph[i][j].up),
                (-1, 0, graph[i][j].lt),
            ]:
                ni = i + y
                nj = j + x
                if -1 < nj < m and -1 < ni < n:
                    cost = bfs((ni, nj), stps - 1) + c
                    if cost < min_cost:
                        min_cost = cost
            dp[prsnt[0]][prsnt[1]][stps] = min_cost
        return dp[prsnt[0]][prsnt[1]][stps]

    for i in range(n):
        for j in range(m):
            val = bfs((i, j), k_steps // 2)
            if val == math.inf:
                ans[i][j] = -1

            else:
                ans[i][j] = val * 2
    return ans

def main(n):
    # Map n to grid size and steps deterministically
    if n <= 0:
        n_rows = n_cols = 1
        k_steps = 1

    else:
        n_rows = max(1, n // 3)
        n_cols = max(1, n - n_rows)
        if n_cols > 3 * n_rows:
            n_cols = 3 * n_rows
        k_steps = max(1, (n_rows + n_cols) // 2)
    graph = build_graph(n_rows, n_cols)
    result = solve(n_rows, n_cols, k_steps, graph)
    for row in result:
        # print(' '.join(str(x) for x in row))
        pass
if __name__ == "__main__":
    main(10)