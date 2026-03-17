def main(n):
    # n is the number of additional points besides the origin
    # deterministic generation of points:
    # origin (x0, y0) = (0, 0)
    # point i (1-based) = (i, i * i)
    x0, y0 = 0, 0
    arr = [[x0, y0]]
    for i in range(1, n + 1):
        x = i
        y = i * i
        arr.append([x, y])

    dist = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            dx = arr[i][0] - arr[j][0]
            dy = arr[i][1] - arr[j][1]
            dist[i][j] = dx * dx + dy * dy

    def dfs(status, memo, pp):
        if memo[status] is not None:
            return memo[status]
        if status < 0:
            return 1e8
        res = 1e8
        prev = []
        for i in range(1, n + 1):
            if (status & (1 << (i - 1))) == 0:
                continue
            t1 = status ^ (1 << (i - 1))
            temp = dfs(t1, memo, pp) + dist[0][i] * 2
            if temp < res:
                res = temp
                prev = [i, 0]
            for j in range(i + 1, n + 1):
                if (t1 & (1 << (j - 1))) == 0:
                    continue
                nxt = t1 ^ (1 << (j - 1))
                temp = dfs(nxt, memo, pp) + dist[0][j] + dist[j][i] + dist[i][0]
                if temp < res:
                    res = temp
                    prev = [i, j, 0]
            break
        memo[status] = res
        pp[status] = prev
        return res

    memo = [None for _ in range(1 << n)]
    pp = [None for _ in range(1 << n)]
    memo[0] = 0
    pp[0] = []
    end = (1 << n) - 1
    res = dfs(end, memo, pp)
    path = [0]
    cur = end
    while cur > 0:
        prev = pp[cur]
        path.extend(prev)
        for i in range(len(prev) - 1):
            cur -= (1 << (prev[i] - 1))

    # print(res)
    # print(" ".join(map(str, path)))


if __name__ == "__main__":
    main(4)