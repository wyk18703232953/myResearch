def main(n):
    if n <= 0:
        return

    # Deterministic generation of xs, ys based on n
    xs = float(n)
    ys = float(n * 2)

    # Deterministic generation of objects:
    # objects[i] = (i, i^2) as floats for i in [0, n-1]
    objects = [[float(i), float(i * i)] for i in range(n)]
    objects.append([xs, ys])  # handbag at index n

    dist = [[0.0] * (n + 1) for _ in range(n + 1)]
    dist2 = [[0.0] * n for _ in range(n)]

    for i in range(n + 1):
        xi, yi = objects[i]
        for j in range(n + 1):
            xj, yj = objects[j]
            dx = xi - xj
            dy = yi - yj
            dist[i][j] = dx * dx + dy * dy

    for i in range(n):
        for j in range(n):
            dist2[i][j] = dist[n][i] + dist[i][j] + dist[j][n]

    dp = [1e6] * (1 << n)
    vis = set([0])
    dp[0] = 0.0

    for i in range((1 << n) - 1):
        if i in vis:
            for j in range(n):
                if i & (1 << j) == 0:
                    newi = i | (1 << j)
                    val1 = dp[i] + 2.0 * dist[n][j]
                    if val1 < dp[newi]:
                        dp[newi] = val1
                    vis.add(newi)

                    for k in range(j + 1, n):
                        if i & (1 << k) == 0:
                            newi2 = newi | (1 << k)
                            val2 = dp[i] + dist2[j][k]
                            if val2 < dp[newi2]:
                                dp[newi2] = val2
                            vis.add(newi2)
                    break

    curr = (1 << n) - 1
    path = [0]
    while curr:
        progressed = False
        for i in range(n):
            if curr & (1 << i):
                prev = curr ^ (1 << i)
                if dp[curr] == dp[prev] + 2.0 * dist[n][i]:
                    path.extend([i + 1, 0])
                    curr = prev
                    progressed = True
                    break

                for j in range(i + 1, n):
                    if curr & (1 << j):
                        prev2 = curr ^ (1 << i) ^ (1 << j)
                        if dp[curr] == dp[prev2] + dist2[i][j]:
                            path.extend([j + 1, i + 1, 0])
                            curr = prev2
                            progressed = True
                            break
                if progressed:
                    break
        if not progressed:
            break

    # print(int(dp[(1 << n) - 1]))
    # print(*path[::-1])


if __name__ == "__main__":
    main(4)